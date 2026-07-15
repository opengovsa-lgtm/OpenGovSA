# OpenGovSA

A citizen transparency platform tracking verified corruption cases, public funds lost, recoveries, and accountability data in South Africa.

## Mission

To provide evidence-based public information from official sources such as SIU reports, Auditor-General reports, court records, and commissions of inquiry.

## Project Structure

```
OpenGovSA/
├── backend/          # FastAPI backend service
├── admin-dashboard/  # Admin dashboard (placeholder)
├── mobile/           # Mobile application (placeholder)
├── ai-engine/        # AI/ML services (placeholder)
├── database/         # Database schemas and documentation (placeholder)
└── docs/             # Project documentation (placeholder)
```

## Current Status

**Phase 1: Backend Scaffold** (in progress)

The backend service is currently in early development with basic infrastructure in place:
- FastAPI application with health endpoints
- Database connection setup (PostgreSQL)
- Alembic migration framework
- CI/CD pipeline with GitHub Actions
- Code quality tooling (Black, Ruff, isort, mypy, pytest)

## Getting Started

### Backend

See [backend/README.md](backend/README.md) for detailed setup instructions.

### Prerequisites

- Python 3.12 (required - not compatible with Python 3.14)
- PostgreSQL 16
- Docker (optional, for containerized deployment)

## Development

The project uses a phased development approach. Currently focused on establishing the backend scaffold with proper security, testing, and CI/CD foundations.

## Contributing

This project is in early development. Contribution guidelines will be established as the codebase matures.

## License

MIT
