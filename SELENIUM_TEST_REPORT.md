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
- Deployment platform tested: Render

## Test coverage

The script `tests/test_poc.py` runs against the deployed frontend, not localhost, and checks:

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
py -u tests/test_poc.py
```

Optional URL overrides:

```powershell
$env:FRONTEND_URL="https://downtime-frontend.onrender.com"
$env:BACKEND_URL="https://downtime-backend.onrender.com"
```

## Execution results

**Overall result: PASS**

- Execution date: 2026-11-03
- Passed: 8
- Failed: 0
- Browser: Google Chrome via Selenium WebDriver
- Headless mode: False
- Frontend: `https://downtime-frontend.onrender.com`
- Backend: `https://downtime-backend.onrender.com`
- Backend API response: HTTP 200
- Incident records returned: 10
- Mobile viewport tested: 390px

### Individual test results

| Test | Result |
|---|---|
| Live dashboard page load | PASS |
| Incident data and visualizations | PASS |
| Frontend-backend API handshake | PASS |
| Machine filter and reset interaction | PASS |
| Intelligence Panel open/close | PASS |
| Project information and developer signature | PASS |
| Responsive layout at mobile width | PASS |
| Desktop screenshot capture | PASS |

## Evidence files

- `screenshots/selenium_dashboard.png`
- `screenshots/selenium_mobile.png`
- `test-results/Test_Report.txt`

The detailed execution output is recorded in `test-results/Test_Report.txt`.

## Deployment limitation

The currently documented live deployment is on **Render**, not Azure Container Apps. Selenium passing against Render demonstrates browser-level functionality of the Render deployment; it does not fulfil a separate Phase 2 Azure Container Apps deployment requirement.

Do not represent this Render validation as Azure deployment validation.