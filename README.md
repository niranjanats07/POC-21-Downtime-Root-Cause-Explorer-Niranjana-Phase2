# POC-21 | Downtime Root Cause Explorer

**Infocreon Internship Project — Phase 2**

An interactive analytics dashboard for exploring machinery downtime, investigating potential root causes, and analysing machine performance.

---

## Project Overview

Downtime Root Cause Explorer is a web-based analytics application designed to help users analyse manufacturing downtime incidents and understand machine performance.

The dashboard combines incident records, key performance indicators, interactive visualisations, and filtering capabilities to provide a centralised view of downtime patterns and potential root causes.

## Key Features

- **Downtime Analytics:** View incident records and key performance indicators.
- **Machine Filtering:** Filter incident records by machine.
- **Interactive Visualisations:** Explore downtime patterns and machine performance through charts.
- **Root Cause Exploration:** Investigate incident details using the Intelligence Panel.
- **Data Export:** Export filtered incident data in CSV and JSON formats.
- **Project Information:** View project and developer details.

## Technology Stack

| Component | Technologies |
|:---|:---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Backend | FastAPI, Python, Pandas, DuckDB |
| Visualisation | Apache ECharts, Plotly, D3.js |
| Data Tables | TanStack Table |
| Containerisation | Docker, Docker Compose |
| Cloud Hosting | Render |
| Automated Testing | Selenium WebDriver 4, Python, Google Chrome |

---

## Project Setup

### Run Locally

**Backend**

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend: `http://localhost:8000`

**Frontend**

Open a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:3000`

### Run with Docker

**Prerequisites:** Docker Desktop and Docker Compose.

Build and start the application from the project root:

```bash
docker compose up --build -d
```

**Application Endpoints**

| Service | Local URL |
|:---|:---|
| Frontend | [http://localhost:3000](http://localhost:3000) |
| Backend API | [http://localhost:8000](http://localhost:8000) |
| Backend Health Check | [http://localhost:8000/health](http://localhost:8000/health) |

**Check container status**

```bash
docker compose ps
```

**View container logs**

```bash
docker compose logs
```

**Stop containers**

```bash
docker compose down
```

**Docker Validation**

Local Docker validation covered application startup, API communication, dashboard loading, incident data, machine filters, charts, exports, and container restart behaviour.

---

## Live Deployment — Render

The application is hosted on Render using Docker-based deployment.

### Application URLs

| Service | Link |
|:---|:---|
| Frontend Dashboard | [Open Dashboard](https://downtime-frontend.onrender.com/) |
| Backend API | [Open Backend API](https://downtime-backend.onrender.com/) |
| Backend Health Check | [Check Health](https://downtime-backend.onrender.com/health) |

### Deployment Configuration

| Setting | Configuration |
|:---|:---|
| Hosting Platform | Render |
| Deployment Method | Docker |
| Git Branch | `main` |
| Region | Singapore |
| Frontend Health Check | `/` |
| Backend Health Check | `/health` |

Frontend and backend deployment, API communication, dashboard data loading, and service restart validation were completed successfully.

### Environment Variables

**Frontend**

```env
NEXT_PUBLIC_API_URL=https://downtime-backend.onrender.com
```

**Backend**

```env
FRONTEND_ORIGIN=https://downtime-frontend.onrender.com
```

---

## Selenium End-to-End Testing

Automated browser testing was performed against the live Render application using Selenium WebDriver 4, Python, and Google Chrome.

### Test Environment

| Configuration | Details |
|:---|:---|
| Framework | Selenium WebDriver 4 |
| Language | Python |
| Browser | Google Chrome |
| Test Script | `tests/test_poc.py` |
| Dependencies | `requirements-test.txt` |
| Test Target | Live Render deployment |

### Live URLs Tested

- **Frontend:** [downtime-frontend.onrender.com](https://downtime-frontend.onrender.com/)
- **Backend:** [downtime-backend.onrender.com](https://downtime-backend.onrender.com/)
- **Health Endpoint:** [Backend Health Check](https://downtime-backend.onrender.com/health)

### Install Dependencies

Run from the Phase 2 repository root:

```bash
py -m pip install -r requirements-test.txt
```

### Execute Tests

```bash
py -u tests/test_poc.py
```

**Run Chrome in visible browser mode using PowerShell:**

```powershell
$env:HEADLESS="false"
py -u tests/test_poc.py
```

### Automated Test Coverage

The Selenium test suite validates:

1. Live application page loading.
2. Incident data retrieval and chart rendering.
3. Frontend-to-backend API communication.
4. Machine filtering and reset functionality.
5. Intelligence Panel interaction.
6. Project information and developer signature.
7. Responsive page-width validation at a 390px viewport.
8. Desktop and mobile screenshot capture.

### Latest Test Results

**Test Status: PASS — 8 Passed, 0 Failed**

| Metric | Result |
|:---|:---|
| Execution Date | 03 November 2026 |
| Execution Time | 05:37:43 UTC |
| Browser | Google Chrome |
| Tests Passed | 8 |
| Tests Failed | 0 |
| Backend API Status | HTTP 200 |
| Incident Records Retrieved | 10 |
| Mobile Viewport | 390px |

The responsive validation confirmed that the document and page widths remained within the 390px viewport. Some internal chart and table content may extend beyond the viewport.

### Test Evidence

- [Selenium Test Script](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/tests/test_poc.py)
- [Test Dependencies](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/requirements-test.txt)
- [Test Execution Report](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/test-results/Test_Report.txt)
- [Desktop Screenshot](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/screenshots/selenium_dashboard.png)
- [Mobile Screenshot](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/screenshots/selenium_mobile.png)
- [Detailed Selenium Test Report](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/blob/main/SELENIUM_TEST_REPORT.md)

---

## Known Limitations

- The application currently uses synthetic downtime incident data.
- Render is used for cloud hosting. Azure Container Apps and Azure Container Registry were not used.
- Selenium validation was performed against the live Render deployment.
- Some chart and table content may require horizontal scrolling on narrow screens.

## Developer Information

| Detail | Information |
|:---|:---|
| Developer | Niranjana T Suresh |
| PoC ID | 21 |
| Organisation | Infocreon |
| Programme | Internship — Phase 2 |
| Batch | Batch 8 / MA College |
| GitHub | [@niranjanats07](https://github.com/niranjanats07) |

## Repository

[**POC-21 — Downtime Root Cause Explorer | Phase 2**](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2)

---

<p align="center">
  <strong>POC-21 | DOWNTIME ROOT CAUSE EXPLORER</strong><br/>
  <sub>Manufacturing Downtime Analytics &amp; Root Cause Exploration</sub><br/>
  <sub>Infocreon Internship Programme — Phase 2</sub>
</p>
