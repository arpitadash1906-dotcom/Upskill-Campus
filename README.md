# TravelGrid

Production-ready full-stack travel platform for trip discovery, booking workflows, AI-assisted planning, itinerary support, travel utilities, and collaborative travel experiences.

[Live demo](https://travel-grid.vercel.app/) | [GitHub repository](https://github.com/arpitadash1906-dotcom/Upskill-Campus)

## Overview

TravelGrid combines a modern React frontend, an Express/MongoDB API, real-time collaboration through Socket.IO, and an optional Python AI planning service. It is designed as a modular travel application where users can explore destinations, manage bookings, plan trips, compare costs, save places, share trips, and use AI-powered travel helpers.

## Core Capabilities

- Destination discovery, travel packages, hotels, rentals, guides, and saved places
- User authentication, email verification, protected routes, and profile management
- Booking, review, wishlist, forum, checklist, mood board, and sharing flows
- Trip expense calculator, visa checker, map-based itinerary views, QR sharing, and PDF generation
- Multi-language frontend support with locale files under `client/src/locales`
- Real-time collaboration features powered by Socket.IO
- AI travel planning service using FastAPI, LangGraph, LangChain, OpenAI, and MCP-style helper services
- API security middleware for sanitization, XSS protection, CORS, Helmet headers, and rate limiting

## Architecture

```text
Browser
  |
  | React + Vite frontend
  v
client/ ------------------------------+
                                      |
                                      v
Server/ Express API + Socket.IO ---> MongoDB
  |
  | Optional AI planning calls
  v
travel-ai-system/
  |-- ai-service/      FastAPI + LangGraph planner
  `-- mcp-servers/    Flights, hotels, places, currency helpers
```

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | React 19, Vite, Tailwind CSS, Redux Toolkit, React Router, MUI, Framer Motion |
| Backend | Node.js, Express, MongoDB, Mongoose, Socket.IO |
| AI service | Python, FastAPI, LangGraph, LangChain, OpenAI, FAISS |
| Security | Helmet, CORS, rate limiting, input sanitization, JWT |
| Utilities | Leaflet, i18next, jsPDF, QR code generation, EmailJS, Nodemailer |
| Tooling | npm, ESLint, Jest, GitHub |

## Repository Structure

```text
TravelGrid/
|-- client/                    # React + Vite application
|-- Server/                    # Express API, Socket.IO, MongoDB models, tests
|-- travel-ai-system/
|   |-- ai-service/            # FastAPI + LangGraph AI planner
|   `-- mcp-servers/           # Travel helper services
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- DEPLOYMENT.md
|-- SECURITY.md
|-- LICENSE
`-- README.md
```

## Prerequisites

- Node.js 18 or newer
- npm 9 or newer
- Python 3.10 or newer, only for the AI service
- MongoDB Atlas or local MongoDB
- API keys for enabled third-party services

## Environment Configuration

Create local environment files from the committed examples:

```bash
cp client/.env.example client/.env
cp Server/.env.example Server/.env
cp travel-ai-system/ai-service/.env.example travel-ai-system/ai-service/.env
```

Important variables:

| File | Variable | Required | Description |
| --- | --- | --- | --- |
| `client/.env` | `VITE_API_URL` | Yes | Base URL for the Express API |
| `Server/.env` | `MONGODB_URI` | Yes | MongoDB connection string |
| `Server/.env` | `JWT_SECRET` | Yes | Secret for signing JWTs |
| `Server/.env` | `PORT` | No | API port, defaults to `5000` |
| `Server/.env` | `RAPIDAPI_KEY` | Feature-based | Train search provider key |
| `Server/.env` | `DATA_GOV_API_KEY` | Feature-based | Bus data provider key |
| `Server/.env` | `AVIATION_API_KEY` | Feature-based | Flight data provider key |
| `travel-ai-system/ai-service/.env` | `OPENAI_API_KEY` | AI only | Enables AI itinerary planning |

Never commit real `.env` files, production secrets, uploaded media, virtual environments, or build output.

## Local Development

Install and start the backend:

```bash
cd Server
npm install
npm run dev
```

Install and start the frontend:

```bash
cd client
npm install
npm run dev
```

Run the optional AI service:

```bash
cd travel-ai-system/ai-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Default local services:

| Service | URL |
| --- | --- |
| Frontend | `http://localhost:5173` |
| Backend API | `http://localhost:5000` |
| API health check | `http://localhost:5000/api/health` |
| AI service | `http://localhost:8000` |

## Available Scripts

Frontend:

```bash
cd client
npm run dev
npm run build
npm run lint
npm run preview
```

Backend:

```bash
cd Server
npm start
npm run dev
npm test
npm run test:watch
```

AI service:

```bash
cd travel-ai-system/ai-service
python -m py_compile main.py
uvicorn main:app --reload --port 8000
```

## API Surface

The Express server mounts the main REST API under `/api`.

Common route groups include:

| Route | Purpose |
| --- | --- |
| `/api/health` | Runtime health check |
| `/api/auth` | Authentication |
| `/api/email` | Email verification |
| `/api/users` | User profile operations |
| `/api/bookings` | Booking workflows |
| `/api/reviews` | Reviews |
| `/api/search` | Search |
| `/api/currency` | Currency utilities |
| `/api/chatbot` | Chatbot flows |
| `/api/checklist` | Travel checklist |
| `/api/trains/search` | Train search |
| `/api/buses/search` | Bus search |
| `/api/flights/search` | Flight search |

The AI planner exposes:

```text
POST /plan
```

from `travel-ai-system/ai-service/main.py`.

## Production Checklist

Before deploying:

- Set `NODE_ENV=production` for the backend.
- Use strong, rotated values for `JWT_SECRET` and API keys.
- Restrict CORS origins to deployed frontend domains.
- Use managed MongoDB with backups enabled.
- Configure HTTPS at the hosting or reverse proxy layer.
- Store uploaded media in object storage instead of the repository.
- Run frontend build and backend tests before release.
- Monitor logs, API errors, rate-limit events, and database connection failures.

More deployment guidance is available in `DEPLOYMENT.md`.

## Quality Gates

Recommended checks before opening a pull request:

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

## Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` before opening a pull request.

Recommended workflow:

1. Create a focused branch from `main`.
2. Make the smallest complete change.
3. Update docs or examples when behavior changes.
4. Run the relevant checks.
5. Open a pull request with a clear summary and verification notes.

## Security

Please do not open public issues for sensitive vulnerabilities. Follow `SECURITY.md` for responsible disclosure.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
