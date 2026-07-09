# OpenGovSA Architecture

## Evidence-First Philosophy

OpenGovSA is built on an evidence-first philosophy. All data entered into the system must be backed by verifiable sources such as:
- SIU (Special Investigating Unit) reports
- Auditor-General reports
- Court records
- Commissions of inquiry findings

This ensures the platform maintains credibility and provides citizens with trustworthy information.

## Layered Architecture

The application follows a layered architecture pattern:

### Core Layer
- **config**: Application configuration using Pydantic Settings
- **database**: SQLAlchemy 2.0 engine and session management
- **logging**: Structured JSON logging configuration
- **security**: Password hashing and security utilities

### API Layer
- **v1**: Versioned API endpoints
  - **health**: Health check endpoints (liveness, readiness)
  - **sources**: Source management endpoints (Batch 2)
  - **evidence**: Evidence management endpoints (Batch 2)
  - **cases**: Case management endpoints (Batch 2)

### Data Layer
- **session**: Database session dependency injection
- **models**: SQLAlchemy ORM models (Batch 2)

## Versioned API

The API is versioned to allow for future evolution without breaking existing clients:
- Current version: `/api/v1`
- Future versions will follow `/api/v2`, `/api/v3`, etc.

## Verification Workflow

Evidence verification is a core workflow:
1. Sources are ingested from official documents
2. Evidence is extracted and linked to sources
3. Cases are built from verified evidence
4. Each piece of evidence maintains a chain of custody to its source

## Plugin Roadmap

The platform will support plugins for:
- Additional data source integrations
- Custom verification workflows
- AI-powered analysis tools
- Third-party API integrations

## Five Batch Roadmap

### Batch 1: Platform Infrastructure (Current)
- Project scaffolding
- Core configuration
- Database setup
- Health endpoints
- CI/CD pipeline
- Docker containerization

### Batch 2: Core Data Models
- Source models
- Evidence models
- Case models
- CRUD endpoints
- Basic validation

### Batch 3: Authentication & Authorization
- User management
- Role-based access control
- JWT authentication
- Permission system

### Batch 4: Plugin System
- Plugin architecture
- Source plugins
- Verification plugins
- Plugin marketplace

### Batch 5: AI Features
- Evidence extraction
- Pattern detection
- Risk scoring
- Automated reporting
