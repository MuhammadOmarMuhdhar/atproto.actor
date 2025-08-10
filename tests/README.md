# Test Suite

Automated tests for all application components.

## Test Categories:
- `testAuth.py` - Authentication and OAuth flow testing
- `testSites.py` - Site creation, updates, and template rendering
- `testTemplates.py` - Template validation and customization
- `testAtproto.py` - ATProto integration and data synchronization

## Testing Stack:
- pytest for test framework
- pytest-asyncio for async test support
- httpx for API endpoint testing
- factory_boy for test data generation
- pytest-cov for coverage reporting

## Running Tests:
```bash
pytest                    # Run all tests
pytest -v                # Verbose output
pytest --cov=app         # With coverage
pytest tests/testAuth.py # Specific test file
```