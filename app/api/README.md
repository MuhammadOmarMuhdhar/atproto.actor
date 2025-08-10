# API Layer

HTTP endpoints and route handlers for all client-facing functionality.

## Modules:
- `auth.py` - ATProto OAuth authentication, login/logout, session management
- `sites.py` - CRUD operations for landing pages (create, read, update, delete)
- `templates.py` - Template selection, customization, and preview endpoints
- `webhooks.py` - ATProto webhook handlers for real-time data synchronization

## Architecture:
- RESTful API design with FastAPI routers
- Request/response validation using Pydantic schemas
- Authentication middleware for protected endpoints
- Error handling and HTTP status codes

## Example Endpoints:
- `POST /auth/login` - Initiate ATProto OAuth flow
- `GET /sites/{site_id}` - Retrieve landing page configuration
- `POST /sites` - Create new landing page
- `PUT /templates/{template_id}` - Update template customization