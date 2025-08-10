# Database Models

SQLAlchemy ORM models defining the database schema and relationships.

## Models:
- `user.py` - User accounts, ATProto DIDs, authentication tokens
- `site.py` - Landing page configurations, template selections, custom domains
- `template.py` - Template definitions, customization options, and metadata
- `subscription.py` - Billing plans, subscription status, and payment history

## Relationships:
- User -> Sites (one-to-many)
- User -> Subscription (one-to-one)
- Site -> Template (many-to-one)
- Site -> CustomDomain (one-to-one, optional)

## Database Features:
- PostgreSQL for ACID compliance and JSON support
- Automatic timestamps (created_at, updated_at)
- Soft deletes for data retention
- Indexes for performance optimization