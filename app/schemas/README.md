# Pydantic Schemas

Request/response validation and serialization schemas.

## Schema Types:
- `user.py` - User registration, profile updates, authentication responses
- `site.py` - Site creation requests, configuration updates, public site data
- `template.py` - Template selection, customization options, preview requests
- `atproto.py` - ATProto data structures (profiles, posts, followers)

## Validation Features:
- Input sanitization and type checking
- Custom validators for ATProto DIDs and handles
- Response serialization with privacy controls
- Error message standardization

## Usage:
```python
from app.schemas.site import SiteCreateRequest, SiteResponse
from app.schemas.user import UserProfile
```