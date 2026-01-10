# Interaction Tracker

A full-stack application where you can log user interactions (clicks, page views, form submissions) and displays them in a dashboard with summary statistics.

## Features

- **Create Interactions**: Submit user interactions with metadata
- **Filter & View**: Filter interactions by user ID or event type
- **Statistics Dashboard**: View total interactions, breakdowns by event type and user, and identify the most active user
- **Persistent Storage**: PostgreSQL database with Docker volume persistence
- **API Documentation**: Interactive API docs at `/docs` (Swagger UI)

## Technologies Used

### Backend

- **FastAPI**: Modern Python web framework
- **Prisma**: Type-safe database ORM
- **PostgreSQL 15**: Relational database
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server

### Frontend

- **React**: UI library with Vite build tool
- **Mantine v7**: Component library and styling

### Testing & Infrastructure

- **pytest**: Backend testing framework
- **Docker & Docker Compose**: Containerization and orchestration

## Project Structure

```text
interaction-tracker/
├── client/              # React frontend
│   ├── src/
│   │   ├── components/  # UI components
│   │   └── api/         # API client functions
│   └── package.json
├── server/              # FastAPI backend
│   ├── src/
│   │   ├── routes/      # API endpoints
│   │   ├── services/    # Business logic
│   │   ├── schemas.py   # Pydantic models
│   │   ├── db.py        # Database client
│   │   └── main.py      # Application entry point
│   ├── prisma/          # Database schema and migrations
|   ├── scripts/
│   └── requirements.txt
├── infra/docker/        # Docker configuration
└── docs/                # Project documentation
```

## Getting Started

### Prerequisites

- **Docker & Docker Compose** (recommended), or:
  - Python 3.11+
  - Node.js 18+
  - PostgreSQL 15+

### Quick Start (Docker)

The easiest way to run the application is with Docker Compose:

```bash
cd interaction-tracker/infra/docker
docker-compose up --build
```

This will:

- Start PostgreSQL on port 5432
- Run database migrations automatically
- Start the FastAPI backend on port 8000
- Preserve data across container restarts

**Access the backend:**

- API: <http://localhost:8000>
- Interactive docs: <http://localhost:8000/docs>

**Start the frontend separately:**

```bash
cd interaction-tracker/client
npm install
npm run dev
```

The frontend will be available at <http://localhost:5173>

**Stop the application:**

```bash
docker-compose down        # Stop containers, keep data
docker-compose down -v     # Stop and delete all data
```

### Manual Setup (Without Docker)

#### 1. Set up PostgreSQL

Create a `.env` file in server:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/interaction_tracker
```

#### 2. Backend Setup

```bash
cd interaction-tracker/server

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
prisma migrate deploy

# Generate prisma client
prisma generate

# Start the server
uvicorn src.main:app --reload
```

Backend will be available at <http://localhost:8000>

#### 3. Frontend Setup

```bash
cd interaction-tracker/client

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at <http://localhost:5173>

## Running Tests

Backend tests use pytest:

```bash
cd interaction-tracker/server
pytest
```

For verbose output:

```bash
pytest -v
```

## Video Demonstration


https://github.com/user-attachments/assets/2c2affd2-ec34-4468-b3a3-3d7dcd05be5e



## API Endpoints

### Create Interaction

```text
POST /api/interactions
Content-Type: application/json

{
  "user_id": "user_123",
  "event_type": "click",
  "metadata": {"button": "submit"}  // optional
}
```

### Get Interactions

```text
GET /api/interactions
GET /api/interactions?user_id=user_123
GET /api/interactions?event_type=click
GET /api/interactions?user_id=user_123&event_type=click
```

### Get Statistics

```text
GET /api/interactions/stats

Returns:
{
  "count": 150,
  "count_by_event_type": [...],
  "count_by_user": [...],
  "most_active_user": {"user_id": "user_123", "count": 45}
}
```

## Development Notes

- **Hot Reload**: Both backend (uvicorn --reload) and frontend (Vite) support hot reload in development
- **Data Persistence**: Docker uses a named volume `postgres_data` to persist database across restarts
- **Database Migrations**: Migrations run automatically on Docker container startup
- **API Validation**: All request bodies validated via Pydantic schemas
- **Enum Synchronization**: `EventType` enum must match in both Prisma schema and Pydantic models

## Troubleshooting

**"Table does not exist" error:**

- Run `prisma migrate deploy` to apply migrations
- With Docker, ensure the container command includes migration step

**Frontend can't connect to backend:**

- Verify backend is running on <http://localhost:8000>
- Check CORS settings if accessing from different origin

**Metadata validation error:**

- Ensure metadata is valid JSON object `{}` or omit entirely
- Empty objects `{}` are valid; strings/arrays are not
