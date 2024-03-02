[![Web testing](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml)

# Test framework based on pytest
Test framework to test backend, frontend and mobile apps

## Patterns:    
- Page Object Model
- Singleton

## Run tests:
```bash
docker compose run --rm testframework -s tests/web/ikea/test_ikea.py --env PROD

pytest -s tests/web/ikea/test_ikea.py --env PROD
```