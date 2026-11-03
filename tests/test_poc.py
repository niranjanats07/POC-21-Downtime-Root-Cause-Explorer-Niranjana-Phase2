"""
PoC 21 - Downtime Root Cause Explorer
Selenium end-to-end tests for the deployed Render application.

Run from the repository root:
    py -m pip install -r requirements-test.txt
    py tests/test_poc.py

Optional environment variables:
    FRONTEND_URL  (default: https://downtime-frontend.onrender.com)
    BACKEND_URL   (default: https://downtime-backend.onrender.com)
    HEADLESS      (default: true; set false to watch the browser)
"""

import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = ROOT / "screenshots"
RESULT_DIR = ROOT / "test-results"

SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "https://downtime-frontend.onrender.com"
).rstrip("/")

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://downtime-backend.onrender.com"
).rstrip("/")

HEADLESS = os.getenv("HEADLESS", "true").lower() not in (
    "0", "false", "no"
)

WAIT_SECONDS = 35

results = []
driver = None


def record(name, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    results.append((name, status, detail))

    print(
        f"[{status}] {name}"
        + (f" — {detail}" if detail else ""),
        flush=True,
    )


def wait_for(condition, description):
    try:
        return WebDriverWait(driver, WAIT_SECONDS).until(condition)
    except TimeoutException as exc:
        raise AssertionError(
            f"Timed out waiting for: {description}"
        ) from exc


def run_check(name, fn):
    try:
        detail = fn()
        record(name, True, str(detail or "Validated"))
    except Exception as exc:
        record(
            name,
            False,
            f"{type(exc).__name__}: {exc}"
        )
        print(traceback.format_exc(), flush=True)


def start_browser():
    options = webdriver.ChromeOptions()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")

    return webdriver.Chrome(options=options)


def check_page_load():
    driver.get(FRONTEND_URL)

    wait_for(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(., 'Downtime Root Cause Explorer')]"
            )
        ),
        "dashboard heading",
    )

    assert "Downtime Root Cause Explorer" in driver.title

    return (
        f"Loaded {FRONTEND_URL}; "
        f"title={driver.title!r}"
    )


def check_data_and_visualizations():
    wait_for(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[contains(., 'Incident Filters')]"
            )
        ),
        "Incident Filters section",
    )

    wait_for(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[contains(., '10 of 10 incidents')]"
            )
        ),
        "10 loaded incidents",
    )

    chart_titles = [
        "Downtime Pareto Analysis",
        "Downtime by Machine",
        "Failure Frequency vs Downtime Duration",
        "Root Cause Tree",
    ]

    visible_titles = []

    for title in chart_titles:
        wait_for(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[normalize-space()='{title}']"
                )
            ),
            title,
        )

        visible_titles.append(title)

    canvases = driver.find_elements(
        By.CSS_SELECTOR,
        "canvas"
    )

    visible_canvases = [
        canvas for canvas in canvases
        if canvas.is_displayed()
    ]

    assert len(visible_canvases) >= 2, (
        "Expected at least 2 visible chart canvases; "
        f"found {len(visible_canvases)}"
    )

    return (
        f"10 incident rows; "
        f"{len(visible_canvases)} visible chart canvases; "
        f"{', '.join(visible_titles)}"
    )


def check_frontend_backend_handshake():
    payload = driver.execute_async_script(
        """
        const url = arguments[0];
        const done = arguments[arguments.length - 1];

        fetch(url, {cache: "no-store"})
          .then(async response => {
            const body = await response.json();

            done({
              ok: response.ok,
              status: response.status,
              count: Array.isArray(body) ? body.length : -1
            });
          })
          .catch(error => {
            done({
              ok: false,
              error: String(error)
            });
          });
        """,
        f"{BACKEND_URL}/api/incidents",
    )

    assert payload.get("ok") is True, (
        f"Backend fetch failed: {payload}"
    )

    assert payload.get("count") == 10, (
        f"Expected 10 incidents from API: {payload}"
    )

    return (
        f"GET {BACKEND_URL}/api/incidents returned "
        f"HTTP {payload['status']} with "
        f"{payload['count']} records"
    )


def check_filter_interaction():
    machine_select = wait_for(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[contains(., 'Machine')]//select"
            )
        ),
        "Machine filter select",
    )

    Select(machine_select).select_by_visible_text("MCH-01")

    wait_for(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(., '3 of 10 incidents')]"
            )
        ),
        "filtered incident count",
    )

    rows = driver.find_elements(
        By.XPATH,
        "//section[.//h2[contains(., 'Incident Investigation')]]"
        "/div//tbody/tr",
    )

    assert len(rows) == 3, (
        f"Expected 3 MCH-01 rows, got {len(rows)}"
    )

    reset = wait_for(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[normalize-space()='Reset filters']"
            )
        ),
        "Reset filters button",
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        reset,
    )

    reset.click()

    wait_for(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(., '10 of 10 incidents')]"
            )
        ),
        "reset incident count",
    )

    return (
        "Machine=MCH-01 reduced list to 3; "
        "Reset filters restored 10"
    )


def check_intelligence_panel():
    investigate_locator = (
        By.XPATH,
        "("
        "//section[.//h2[contains(., 'Incident Investigation')]]"
        "//button[normalize-space()='Investigate']"
        ")[1]",
    )

    first_investigate = wait_for(
        EC.presence_of_element_located(
            investigate_locator
        ),
        "first Investigate button",
    )

    driver.execute_script(
        """
        arguments[0].scrollIntoView({
            behavior: 'instant',
            block: 'center',
            inline: 'nearest'
        });
        """,
        first_investigate,
    )

    first_investigate = wait_for(
        EC.element_to_be_clickable(
            investigate_locator
        ),
        "clickable Investigate button",
    )

    try:
        first_investigate.click()

    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            first_investigate,
        )

        first_investigate = wait_for(
            EC.element_to_be_clickable(
                investigate_locator
            ),
            "Investigate button after scrolling",
        )

        first_investigate.click()

    dialog = wait_for(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "[role='dialog'][aria-modal='true']",
            )
        ),
        "Intelligence Panel dialog",
    )

    assert "Incident Investigation" in dialog.text, (
        "Incident Investigation text not found in panel"
    )

    assert "Management investigation recommendation" in dialog.text, (
        "Management investigation recommendation not found"
    )

    close_button = wait_for(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-label='Close panel']"
            )
        ),
        "Close panel button",
    )

    close_button.click()

    wait_for(
        EC.invisibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "[role='dialog'][aria-modal='true']",
            )
        ),
        "Intelligence Panel close",
    )

    return (
        "Investigate opened incident details and recommendation; "
        "Close panel dismissed it"
    )


def check_project_information_signature():
    info_locator = (
        By.CSS_SELECTOR,
        "button[aria-label='Open project information']"
    )

    # Return to the top of the page.
    driver.execute_script(
        "window.scrollTo({top: 0, left: 0, behavior: 'instant'});"
    )

    # Locate the project information button.
    info_button = wait_for(
        EC.presence_of_element_located(info_locator),
        "project information icon",
    )

    # Bring the button into the visible viewport.
    driver.execute_script(
        """
        arguments[0].scrollIntoView({
            behavior: 'instant',
            block: 'center',
            inline: 'center'
        });
        """,
        info_button,
    )

    info_button = wait_for(
        EC.visibility_of_element_located(info_locator),
        "visible project information icon",
    )

    # JavaScript click avoids Selenium viewport interception.
    driver.execute_script(
        "arguments[0].click();",
        info_button,
    )

    modal_locator = (
        By.CSS_SELECTOR,
        "[role='dialog'][aria-labelledby='project-information-title']"
    )

    modal = wait_for(
        EC.visibility_of_element_located(modal_locator),
        "Project Information modal",
    )

    modal_text = modal.text.lower()

    assert "niranjana" in modal_text, (
        "Developer name not found"
    )

    assert "21" in modal_text, (
        "PoC ID not found"
    )

    assert "niranjanats07" in modal_text, (
        "GitHub username not found"
    )

    close_locator = (
        By.CSS_SELECTOR,
        "button[aria-label='Close project information']"
    )

    close_button = wait_for(
        EC.presence_of_element_located(close_locator),
        "Close project information button",
    )

    driver.execute_script(
        "arguments[0].click();",
        close_button,
    )

    wait_for(
        EC.invisibility_of_element_located(modal_locator),
        "Project Information modal close",
    )

    return (
        "Info icon opened modal with developer name, "
        "PoC ID 21 and GitHub username"
    )


def check_responsive_layout():
    # Emulate a genuine 390 x 844 CSS-pixel mobile viewport.
    driver.execute_cdp_cmd(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": 390,
            "height": 844,
            "deviceScaleFactor": 1,
            "mobile": True,
        },
    )

    try:
        wait_for(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h1[contains(., 'Downtime Root Cause Explorer')]"
                )
            ),
            "mobile dashboard heading",
        )

        driver.execute_script("window.scrollTo(0, 0)")

        dimensions = driver.execute_script("""
            return {
                viewport: window.innerWidth,
                document: document.documentElement.clientWidth,
                page: document.documentElement.scrollWidth,
                body: document.body.scrollWidth
            };
        """)

        offenders = driver.execute_script("""
            return Array.from(document.querySelectorAll('body *'))
              .map(el => {
                const r = el.getBoundingClientRect();
                return {
                  tag: el.tagName,
                  id: el.id,
                  className: typeof el.className === 'string'
                    ? el.className : '',
                  left: Math.round(r.left),
                  right: Math.round(r.right),
                  width: Math.round(r.width)
                };
              })
              .filter(el =>
                el.right > 392 || el.left < -2
              )
              .sort((a, b) => b.right - a.right)
              .slice(0, 15);
        """)

        driver.save_screenshot(
            str(SCREENSHOT_DIR / "selenium_mobile.png")
        )

        print("MOBILE DIMENSIONS:", dimensions)
        print("MOBILE OVERFLOW ELEMENTS:", offenders)

        assert dimensions["viewport"] == 390, (
            f"Expected 390px mobile viewport: {dimensions}"
        )

        assert dimensions["document"] <= 392, (
            f"Document exceeds mobile viewport: {dimensions}"
        )

        assert dimensions["page"] <= 392, (
            f"Page has horizontal overflow: {dimensions}; "
            f"Elements: {offenders}"
        )

        assert dimensions["body"] <= 392, (
            f"Body has horizontal overflow: {dimensions}; "
            f"Elements: {offenders}"
        )

        return (
            f"390px mobile viewport; "
            f"document width {dimensions['page']}px; "
            "mobile screenshot saved"
        )

    finally:
        # Restore normal desktop browser metrics.
        driver.execute_cdp_cmd(
            "Emulation.clearDeviceMetricsOverride",
            {},
        )
        driver.set_window_size(1440, 1000)


def save_desktop_screenshot():
    driver.set_window_size(1440, 1000)

    driver.execute_script(
        "window.scrollTo(0, 0)"
    )

    driver.save_screenshot(
        str(SCREENSHOT_DIR / "selenium_dashboard.png")
    )

    return "Saved screenshots/selenium_dashboard.png"


def write_report():
    passed = sum(
        1 for _, status, _ in results
        if status == "PASS"
    )

    failed = sum(
        1 for _, status, _ in results
        if status == "FAIL"
    )

    overall = (
        "PASS"
        if failed == 0 and passed == len(results)
        else "FAIL"
    )

    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "POC 21 — DOWNTIME ROOT CAUSE EXPLORER",
        "SELENIUM LIVE APPLICATION TEST REPORT",
        "=" * 58,
        f"Execution time: {timestamp}",
        f"Frontend URL: {FRONTEND_URL}",
        f"Backend URL: {BACKEND_URL}",
        "Deployment platform: Render (not Azure Container Apps)",
        "Browser: Google Chrome via Selenium WebDriver",
        f"Headless: {HEADLESS}",
        "",
        "TEST RESULTS",
        "-" * 58,
    ]

    for name, status, detail in results:
        lines.append(f"{status}: {name}")

        if detail:
            lines.append(f"  {detail}")

    lines += [
        "",
        f"Passed: {passed}",
        f"Failed: {failed}",
        f"Overall Selenium result: {overall}",
        "",
        "Evidence files:",
        "- screenshots/selenium_dashboard.png",
        "- screenshots/selenium_mobile.png",
        "",
        "Important:",
        "This report reflects only checks actually executed.",
        "A passing Render test does not satisfy a separate "
        "Azure Container Apps deployment requirement.",
    ]

    report_path = RESULT_DIR / "Test_Report.txt"

    report_path.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    return overall, passed, failed


def main():
    global driver

    try:
        driver = start_browser()

        run_check(
            "Live page load",
            check_page_load,
        )

        run_check(
            "Incident data and visualizations",
            check_data_and_visualizations,
        )

        run_check(
            "Frontend-backend API handshake",
            check_frontend_backend_handshake,
        )

        run_check(
            "Machine filter and reset interaction",
            check_filter_interaction,
        )

        run_check(
            "Intelligence Panel open/close interaction",
            check_intelligence_panel,
        )

        run_check(
            "Project information icon and developer signature",
            check_project_information_signature,
        )

        run_check(
            "Responsive layout at mobile width",
            check_responsive_layout,
        )

        run_check(
            "Desktop screenshot capture",
            save_desktop_screenshot,
        )

    except WebDriverException as exc:
        record(
            "Browser startup/session",
            False,
            str(exc),
        )

        print(
            "Ensure Google Chrome is installed and "
            "Selenium Manager can obtain a matching driver."
        )

    finally:
        if driver:
            driver.quit()

        overall, passed, failed = write_report()

        print(
            f"\nOverall Selenium result: "
            f"{overall} ({passed} passed, {failed} failed)"
        )

        print(
            f"Report: {RESULT_DIR / 'Test_Report.txt'}"
        )

        sys.exit(
            0 if overall == "PASS" else 1
        )


if __name__ == "__main__":
    main()