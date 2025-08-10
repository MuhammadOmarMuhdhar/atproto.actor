# App Core

Main application package containing all business logic and API endpoints.

## Structure:
- `main.py` - FastAPI application entry point and route registration
- `config.py` - Environment variables, settings, and configuration management
- `database.py` - SQLAlchemy database connection and session management
- `dependencies.py` - Common FastAPI dependencies (auth, database sessions)

## Key Responsibilities:
- Application bootstrap and configuration
- Database connection management
- Dependency injection setup
- Environment-specific settings (dev/staging/prod)

## Usage:
```python
from app.main import app
from app.config import settings
from app.database import get_db
```