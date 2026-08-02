# TravelGrid

TravelGrid is a full-stack travel planning platform for discovering destinations, planning trips, and working with travel services from one place. The project includes a React frontend, an Express/MongoDB backend, and an optional FastAPI-based AI travel planning service.

[Live demo](https://travel-grid.vercel.app/) | [Repository](https://github.com/Adarsh-Chaubey03/TravelGrid)

## Features

- Destination discovery and travel planning workflows
- Flight, hotel, vehicle, and guide-oriented booking experiences
- AI-powered itinerary, budget, and recommendation support
- Authentication-ready backend with JWT, cookies, validation, and security middleware
- Responsive React UI built with Vite and Tailwind CSS
- Optional MCP-style travel data services for flights, hotels, places, and currency

## Tech Stack

| Area | Technologies |
| --- | --- |
| Frontend | React, Vite, Tailwind CSS, Redux Toolkit, React Router |
| Backend | Node.js, Express, MongoDB, Mongoose, Socket.IO |
| AI service | Python, FastAPI, LangGraph, LangChain, OpenAI |
| Tooling | ESLint, Prettier-compatible formatting, Git, GitHub |

## Project Structure

```text
TravelGrid/
|-- client/                    # React + Vite frontend
|-- Server/                    # Express + MongoDB backend
|-- travel-ai-system/
|   |-- ai-service/            # FastAPI/LangGraph travel planner
|   `-- mcp-servers/           # Currency, flight, hotel, and place services
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- LICENSE
`-- README.md
```

## Prerequisites

- Node.js 18 or newer
- npm
- Python 3.10 or newer, for the optional AI service
- MongoDB connection string
- API keys for any external providers you enable

## Environment Variables

Create local `.env` files from the examples before running the services.

```bash
cp client/.env.example client/.env
cp Server/.env.example Server/.env
cp travel-ai-system/ai-service/.env.example travel-ai-system/ai-service/.env
```

Common values:

| File | Variable | Purpose |
| --- | --- | --- |
| `client/.env` | `VITE_API_URL` | Backend API base URL |
| `Server/.env` | `MONGODB_URI` | MongoDB connection string |
| `Server/.env` | `JWT_SECRET` | Secret used to sign JWTs |
| `Server/.env` | `PORT` | Backend port, defaults to `5000` |
| `travel-ai-system/ai-service/.env` | `OPENAI_API_KEY` | Enables AI itinerary planning |

## Getting Started

Install and run the frontend:

```bash
cd client
npm install
npm run dev
```

Install and run the backend:

```bash
cd Server
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

Default local URLs:

| Service | URL |
| --- | --- |
| Frontend | `http://localhost:5173` |
| Backend | `http://localhost:5000` |
| AI service | `http://localhost:8000` |

## Scripts

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
```

## API Notes

- Backend API routes are served from the Express application in `Server/`.
- The AI planner exposes `POST /plan` from `travel-ai-system/ai-service/main.py`.
- MCP server modules live under `travel-ai-system/mcp-servers/` and can be run or wired into the AI service as needed.

## Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` before opening an issue or pull request.

Recommended flow:

1. Fork the repository.
2. Create a feature branch.
3. Install dependencies for the service you are changing.
4. Run the relevant lint, build, or test command.
5. Open a pull request with a clear description and linked issue.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
