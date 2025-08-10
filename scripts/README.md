# Utility Scripts

Administrative and deployment scripts for common tasks.

## Scripts:
- `setupDb.py` - Database initialization and seed data creation
- `syncAtprotoData.py` - Manual ATProto data synchronization
- `deploy.py` - Deployment automation and environment setup

## Usage:
```bash
python scripts/setupDb.py --env=development
python scripts/syncAtprotoData.py --user-id=123
python scripts/deploy.py --environment=staging
```

## Development Workflow:
1. Run `setupDb.py` for local development
2. Use `syncAtprotoData.py` for testing data updates
3. Deploy with `deploy.py` for consistent deployments

## Environment Variables:
Scripts read from `.env` files and respect environment-specific configurations.