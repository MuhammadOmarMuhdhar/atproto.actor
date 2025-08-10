# Service Layer

Business logic services that orchestrate between API, database, and external services.

## Services:
- `authService.py` - User authentication, OAuth flows, session management
- `siteService.py` - Landing page CRUD, template application, domain setup
- `templateService.py` - Template management, customization logic, previews
- `billingService.py` - Stripe integration, subscription management, payments
- `syncService.py` - ATProto data synchronization, periodic updates

## Design Pattern:
- Service classes with dependency injection
- Separation of concerns (database, external APIs, business logic)
- Transaction management and error handling
- Caching layer for frequently accessed data

## Example:
```python
class SiteService:
    def create_site(self, user_id: int, template_id: int) -> Site:
        # Business logic for site creation
```