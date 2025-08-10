# Database Migrations

Database schema migrations using Alembic (SQLAlchemy's migration tool).

## Migration Files:
- `001_initialTables.py` - Initial database schema creation
- Future migrations for schema updates and data transformations

## Migration Process:
1. Generate migration: `alembic revision --autogenerate -m "description"`
2. Review generated SQL
3. Apply migration: `alembic upgrade head`
4. Rollback if needed: `alembic downgrade -1`

## Best Practices:
- Always review auto-generated migrations
- Include data migration scripts when needed
- Test migrations on staging before production
- Backup database before major schema changes