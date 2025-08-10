# Core Business Logic

Central business logic and external service integrations.

## Modules:
- `atprotoClient.py` - ATProto SDK wrapper with authentication and data fetching
- `siteGenerator.py` - Template rendering engine using Jinja2
- `domainManager.py` - Custom domain configuration and DNS management
- `backgroundTasks.py` - Async task handlers for data sync and site generation

## Key Functions:
- ATProto API communication and data synchronization
- HTML template rendering with dynamic content
- Domain routing and SSL certificate management
- Background job processing (Cloud Tasks integration)

## Dependencies:
- ATProto Python SDK for Bluesky integration
- Jinja2 for template rendering
- Google Cloud Tasks for async processing
- Cloudflare API for domain management