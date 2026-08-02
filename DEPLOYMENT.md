# Deployment Guide

This guide summarizes a practical production deployment for TravelGrid.

## Services

TravelGrid can be deployed as two required services and one optional service:

| Service | Path | Runtime | Required |
| --- | --- | --- | --- |
| Frontend | `client/` | Static Vite build | Yes |
| Backend API | `Server/` | Node.js process | Yes |
| AI planner | `travel-ai-system/ai-service/` | FastAPI process | Optional |

## Frontend

Build command:

```bash
cd client
npm ci
npm run build
```

Output directory:

```text
client/dist
```

Required environment:

```text
VITE_API_URL=https://your-api-domain.example.com/api
```

Recommended hosts include Vercel, Netlify, Cloudflare Pages, or any static hosting service that supports single-page application fallback routing.

## Backend API

Install and start:

```bash
cd Server
npm ci
npm start
```

Required environment:

```text
NODE_ENV=production
PORT=5000
MONGODB_URI=mongodb+srv://...
JWT_SECRET=replace-with-a-strong-secret
```

Feature-based environment:

```text
RAPIDAPI_KEY=
DATA_GOV_API_KEY=
AVIATION_API_KEY=
```

Production notes:

- Run behind HTTPS.
- Restrict CORS to trusted frontend domains.
- Use process management such as PM2, Docker, Render, Railway, Fly.io, or a managed Node.js platform.
- Enable MongoDB backups and connection monitoring.
- Do not store uploaded files in Git. Use object storage for persistent user media.

## AI Planner

Install and start:

```bash
cd travel-ai-system/ai-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Required environment:

```text
OPENAI_API_KEY=
```

Production notes:

- Put the service behind a private network or API gateway when possible.
- Add authentication before exposing it publicly.
- Configure request timeouts and logging at the hosting layer.
- Keep vector indexes and generated cache files outside the repository.

## Release Checklist

Before each release:

```bash
cd client
npm run lint
npm run build
```

```bash
cd Server
npm test
```

```bash
cd travel-ai-system/ai-service
python -m compileall . -q
```

Then verify:

- `/api/health` returns a successful response.
- Authentication and protected routes work.
- CORS allows only trusted frontend domains.
- Required API keys are present in the hosting environment.
- Logs do not expose tokens, passwords, cookies, or full connection strings.
