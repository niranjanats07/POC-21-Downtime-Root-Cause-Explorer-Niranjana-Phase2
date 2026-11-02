# POC-21: Downtime Root Cause Explorer

**Infocreon Internship Project — Phase 2**

An interactive dashboard for exploring machinery downtime incidents, identifying root causes, and analysing machine performance.

## Features

- View downtime incidents and key performance indicators.
- Filter incidents by machine.
- Explore downtime using interactive charts.
- Investigate incident details through the Intelligence Panel.
- Export filtered incident data as CSV or JSON.
- View project and developer information.

## Technology Stack

- **Frontend:** Next.js, React, TypeScript, Tailwind CSS
- **Backend:** FastAPI, Python, Pandas, DuckDB
- **Visualisation:** Apache ECharts, Plotly, D3.js
- **Tables:** TanStack Table
- **Containerisation:** Docker, Docker Compose
- **Cloud Deployment:** Render

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
├── .dockerignore
├── .env.example
├── docker-compose.yml
├── .gitignore
├── render.yaml
└── README.md
```

## Running Locally Without Docker

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend: http://localhost:8000

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

## Running with Docker

### Prerequisites

- Docker Desktop installed and running.
- Docker Compose available.

### Environment Configuration

The project includes an `.env.example` template containing the frontend and backend port and API URL settings.

The current Compose configuration publishes the backend on port `8000` and frontend on port `3000`.

### Build and Start Containers

Run these commands from the Phase 2 project root:

```bash
docker compose up --build -d
```

### Check Container Status

```bash
docker compose ps
```

### Access the Application

- **Frontend dashboard:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **Backend health check:** http://localhost:8000/health
- **Dashboard KPI endpoint:** http://localhost:8000/api/dashboard/kpis

### Stop Containers

```bash
docker compose down
```

### Restart Containers

```bash
docker compose restart
```

### View Container Logs

```bash
docker compose logs
```

For backend-only logs:

```bash
docker compose logs backend
```

For frontend-only logs:

```bash
docker compose logs frontend
```

## Docker Validation Results

The following checks were completed in the local Docker environment:

| Validation | Result |
|---|---|
| Backend container startup | Passed |
| Frontend container startup | Passed |
| Backend health endpoint | Passed |
| Frontend dashboard loading | Passed |
| Frontend-to-backend communication | Passed |
| Synthetic incident data loading | Passed |
| Machine filters | Passed |
| Charts and visualisations | Passed |
| Intelligence Panel | Passed |
| CSV and JSON exports | Passed |
| Container restart validation | Passed |

Both containers were confirmed running, with the frontend exposed on port `3000` and backend on port `8000`.

## Render Cloud Deployment

The Phase 2 application was deployed successfully using Render as the coordinator-approved alternative to Azure Container Apps.

### Live Application

- **Frontend Dashboard:** https://downtime-frontend.onrender.com
- **Backend API:** https://downtime-backend.onrender.com
- **Backend Health Check:** https://downtime-backend.onrender.com/health

### Deployment Configuration

| Component | Configuration |
|---|---|
| Frontend | Render Web Service |
| Backend | Render Web Service |
| Deployment Method | Docker |
| Git Branch | main |
| Region | Singapore |
| Frontend Health Check | `/` |
| Backend Health Check | `/health` |

### Environment Configuration

Frontend Render environment variable:

```env
NEXT_PUBLIC_API_URL=https://downtime-backend.onrender.com
```

Backend Render environment variable:

```env
FRONTEND_ORIGIN=https://downtime-frontend.onrender.com
```

### Cloud Validation Results

| Validation | Result |
|---|---|
| Frontend deployment | Passed |
| Backend deployment | Passed |
| Backend health check | Passed |
| Frontend-to-backend communication | Passed |
| Dashboard data loading | Passed |
| Machine filters and visualisations | Passed |
| Incident data display | Passed |
| Frontend restart validation | Passed |
| Backend restart validation | Passed |
| Dashboard revalidation after restart | Passed |

The dashboard was rechecked after restarting both Render services. Incident data, KPI cards, machine breakdowns, charts, and visualisations loaded successfully.

### Cloud Deployment Note

Render was used as the coordinator-approved alternative for the cloud deployment requirement.

- **Azure Container Apps:** Not used.
- **Azure Container Registry:** Not used.
- **Cloud Hosting Platform:** Render.
- **Render Region:** Singapore.

## Troubleshooting

### Docker Desktop is not running

Start Docker Desktop and wait until its engine is ready.

### Port already in use

Check whether another application is using ports `3000` or `8000`. Stop the conflicting application before starting the containers.

### Frontend or backend container is not running

Check the logs:

```bash
docker compose logs
```

Rebuild and restart:

```bash
docker compose down
docker compose up --build -d
```

### Cloud dashboard cannot load backend data

Check that:

- The backend Render service is live.
- The backend health endpoint returns a healthy response.
- The frontend has the correct `NEXT_PUBLIC_API_URL`.
- The backend has the correct `FRONTEND_ORIGIN`.

## Known Limitations

- The project uses synthetic downtime incident data.
- Render was used as the coordinator-approved alternative to Azure Container Apps.
- Azure Container Apps and Azure Container Registry were not used.
- The application was validated through local Docker deployment and the live Render deployment.
- Selenium validation has not been performed.

## Developer Details

- **Developed by:** Niranjana T Suresh
- **PoC ID:** 21
- **GitHub:** [niranjanats07](https://github.com/niranjanats07)
- **Batch:** Batch 8 / MA College
- **Organisation:** Infocreon Internship

## Phase 2 Repository

[POC-21 Downtime Root Cause Explorer — Phase 2](https://github.com/niranjanats07/POC-21-Downtime-Root-Cause-Explorer-Niranjana-Phase2)

---


*Downtime Root Cause Explorer — Machinery & Asset Utilization*
