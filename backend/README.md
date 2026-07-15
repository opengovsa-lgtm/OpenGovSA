# OpenGovSA Backend

A citizen transparency platform tracking verified corruption cases, public funds lost, recoveries, and accountability data in South Africa.

## Mission

To provide evidence-based public information from official sources such as SIU reports, Auditor-General reports, court records, and commissions of inquiry.

## Tech Stack

- **Python 3.12** (Required - not compatible with Python 3.14)
- **FastAPI** - Web framework
- **SQLAlchemy 2.0** - ORM
- **Alembic** - Database migrations
- **Pydantic v2** - Data validation
- **pytest** - Testing
- **Ruff** - Linting
- **Black** - Code formatting
- **isort** - Import sorting
- **mypy** - Type checking
- **Docker** - Containerization
- **GitHub Actions** - CI/CD

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** This project requires Python 3.12. It is not compatible with Python 3.14 due to package dependency constraints. On Windows, some packages may require Visual Studio Build Tools for compilation. For local development on Windows, consider using Docker or WSL2 with Python 3.12.

## Configuration

Copy `.env.example` to `.env` and configure your environment variables:

```bash
cp .env.example .env
```

**Important Security Notes:**
- `SECRET_KEY` must be changed to a cryptographically secure random string in production
- `DATABASE_URL` should use environment-specific credentials
- CORS origins should be restricted to specific domains in production

## Running the Application

```bash
# Development
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Running Tests

```bash
pytest
```

## Code Quality

```bash
# Format code
black .
isort .

# Lint
ruff check .

# Type check
mypy .
```

## Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run tests in Docker
docker-compose run backend pytest
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Health Endpoints

- `GET /api/v1/health` - General health check
- `GET /api/v1/health/live` - Liveness probe
- `GET /api/v1/health/ready` - Readiness probe

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── core/                # Core functionality
│   │   ├── config.py        # Configuration
│   │   ├── database.py      # Database setup
│   │   ├── logging.py       # Logging configuration
│   │   └── security.py      # Security utilities
│   ├── api/                 # API endpoints
│   │   └── v1/
│   │       ├── router.py    # API v1 router
│   │       └── endpoints/
│   │           └── health.py
│   └── db/                  # Database
│       └── session.py       # Session management
├── tests/                   # Tests
│   ├── conftest.py
│   └── test_health.py
├── docs/                    # Documentation
│   └── architecture.md
├── alembic/                 # Database migrations
├── .github/workflows/       # CI/CD
│   └── backend.yml
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

## License

MIT
