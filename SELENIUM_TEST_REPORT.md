# PoC 21 — Selenium Live Application Test Report

## Application details

- Developer: Niranjana T Suresh
- GitHub: `niranjanats07`
- PoC: 21 — Downtime Root Cause Explorer
- Repository: https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2
- Live frontend (Render): https://downtime-frontend.onrender.com
- Backend API: https://downtime-backend.onrender.com
- Browser: Google Chrome
- Automation: Selenium WebDriver 4

## Test coverage

The script `tests/test_poc.py` runs against the deployed frontend (not localhost) and checks:

1. Live dashboard page load and title.
2. Incident data count and chart rendering.
3. Browser-side request to the deployed backend `/api/incidents` endpoint.
4. Machine filter and Reset filters interaction.
5. Incident Investigation / Intelligence Panel open and close.
6. Project information icon, developer name, PoC ID and GitHub username.
7. Responsive layout at a 390px viewport.
8. Desktop and mobile screenshot capture.

## Execution

From the repository root:

```powershell
py -m pip install -r requirements-test.txt
py tests/test_poc.py
```

To see the browser while the test runs:

```powershell
$env:HEADLESS="false"
py tests/test_poc.py
```

Optional URL overrides:

```powershell
$env:FRONTEND_URL="https://downtime-frontend.onrender.com"
$env:BACKEND_URL="https://downtime-backend.onrender.com"
```

## Execution status

**NOT RUN YET.** Run the script on a machine with Google Chrome installed and update this section only from the generated `test-results/Test_Report.txt`.

Expected evidence paths after a successful run:

- `screenshots/selenium_dashboard.png`
- `screenshots/selenium_mobile.png`
- `test-results/Test_Report.txt`

## Deployment limitation

The currently documented live deployment is on **Render**, not Azure Container Apps. Selenium passing against Render demonstrates browser-level functionality of the Render deployment; it does not fulfil the separate Phase 2 Azure Container Apps deployment requirement. State this limitation honestly in the submission unless an Azure deployment is completed.
