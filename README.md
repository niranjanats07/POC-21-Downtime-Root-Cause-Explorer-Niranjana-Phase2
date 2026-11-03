# POC-21: Downtime Root Cause Explorer

**Manufacturing Analytics Dashboard | Infocreon Internship — Phase 2**

An interactive web application for monitoring machinery downtime, exploring incident data, identifying potential root causes, and analysing machine performance.

## Project Overview

The Downtime Root Cause Explorer provides an interactive dashboard for analysing synthetic manufacturing downtime data. It brings together incident records, key performance indicators, machine-level filters, visualisations, and an Intelligence Panel to support downtime investigation.

## Key Features

- **Downtime Monitoring:** View incident records and key performance indicators.
- **Machine Filtering:** Filter incidents by machine.
- **Interactive Visualisations:** Explore downtime patterns, machine performance, and root-cause insights.
- **Intelligence Panel:** Investigate incident details.
- **Data Export:** Export filtered incident data in CSV and JSON formats.
- **Project Information:** View project and developer details.

## Technology Stack

| Component | Technologies |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Backend | FastAPI, Python |
| Data Processing | Pandas, DuckDB |
| Visualisation | Apache ECharts, Plotly, D3.js |
| Data Tables | TanStack Table |
| Containerisation | Docker, Docker Compose |
| Cloud Hosting | Render |
| Automated Testing | Selenium WebDriver 4, Python, Google Chrome |

## Project Structure

```text
POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2/
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── data/
│   └── synthetic/
├── tests/
│   └── test_poc.py
├── screenshots/
├── test-results/
├── docker-compose.yml
├── render.yaml
├── requirements-test.txt
└── README.md
```

## Installation and Setup

### Prerequisites

- Python
- Node.js and npm
- Docker Desktop (for containerised deployment)

### Local Development

**1. Start the backend**

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend: http://localhost:8000

**2. Start the frontend**

Open a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

### Docker Deployment

Run the following commands from the project root.

**Build and start containers**

```bash
docker compose up --build -d
```

**Check container status**

```bash
docker compose ps
```

**Access the application**

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend health check: http://localhost:8000/health

**View logs**

```bash
docker compose logs
```

**Stop containers**

```bash
docker compose down
```

## Live Application

The application is hosted on Render.

| Service | URL |
|---|---|
| Frontend Dashboard | https://downtime-frontend.onrender.com |
| Backend API | https://downtime-backend.onrender.com |
| Backend Health Check | https://downtime-backend.onrender.com/health |

**Deployment configuration**

- Hosting platform: Render
- Deployment method: Docker
- Git branch: `main`
- Region: Singapore
- Frontend health check: `/`
- Backend health check: `/health`

### Environment Variables

Configure the frontend and backend services with the appropriate deployment URLs.

**Frontend**

```env
NEXT_PUBLIC_API_URL=https://downtime-backend.onrender.com
```

**Backend**

```env
FRONTEND_ORIGIN=https://downtime-frontend.onrender.com
```

## Testing and Validation

### Docker Validation

The local Docker deployment was checked for:

- Backend and frontend container startup
- Backend health endpoint
- Dashboard loading and API communication
- Synthetic incident data loading
- Machine filters and visualisations
- Intelligence Panel functionality
- CSV and JSON exports
- Container restart behaviour

### Selenium Automated Testing

Automated browser testing was performed against the live Render deployment using Selenium WebDriver 4, Python, and Google Chrome.

<text-placeholder/>

**Latest test execution: 3 November 2026**

| Test Area | Result |
|---|---|
| Live dashboard loading | Passed |
| Incident data and visualisations | Passed |
| Frontend-backend API communication | Passed |
| Machine filter and reset | Passed |
| Intelligence Panel | Passed |
| Project information and developer details | Passed |
| Responsive page layout at 390px | Passed |
| Screenshot capture | Passed |

**Overall Result: 8 Passed, 0 Failed**

The API returned HTTP 200 with 10 incident records. The responsive test confirmed that the document and page width remained within the 390px mobile viewport; some internal chart and table content may extend beyond that width.

### Test Execution

Install the test dependencies:

```bash
py -m pip install -r requirements-test.txt
```

Run the Selenium test suite:

```bash
py -u tests/test_poc.py
```

### Testing Evidence

- [Selenium Test Report](SELENIUM_TEST_REPORT.md)
- [Test Execution Results](test-results/Test_Report.txt)
- [Desktop Dashboard Screenshot](screenshots/selenium_dashboard.png)
- [Mobile Dashboard Screenshot](screenshots/selenium_mobile.png)
- [Selenium Test Script](tests/test_poc.py)

## Deployment Notes and Limitations

- The project uses synthetic downtime incident data.
- Render is the cloud hosting platform used for this deployment.
- Azure Container Apps and Azure Container Registry were not used.
- Selenium validation was performed against the live Render application.
- The mobile layout test confirms page-level width, but some chart and table content may require further horizontal overflow improvements.

## Developer Information

| Detail | Information |
|---|---|
| Developer | Niranjana T Suresh |
| Proof of Concept | POC-21 |
| GitHub | [@niranjanats07](https://github.com/niranjanats07) |
| Batch | Batch 8 — MA College |
| Organisation | Infocreon |
| Project Phase | Phase 2 |

## Source Code

**GitHub Repository:**  
[POC-21 — Downtime Root Cause Explorer](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2)

---

<p align="center">
  <strong>Downtime Root Cause Explorer</strong><br/>
  <sub>Machinery Downtime Analysis · Root Cause Exploration · Manufacturing Analytics</sub><br/>
  <sub>Infocreon Internship Programme — Phase 2</sub>
</p>
