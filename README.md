[![Web testing](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml)

# Test framework based on pytest
Test framework to test backend, frontend and mobile apps

## Dependencies:
- Python 3.11 and above
- Docker
- Allure (install [allure command line tool](https://allurereport.org/docs/gettingstarted-installation/))
- Pytest
- Selenium
- Poetry

## Patterns:    
- Page Object Model

## Run tests:
```bash
docker compose run --rm testframework -s tests/web/ikea/test_ikea.py --env PROD

pytest -s tests/web/ikea/test_ikea.py --env PROD

pytest -m cookies -s tests/web/ikea/test_ikea.py --env PROD
```

## Check Allure reports:
```bash
allure serve allure-results
```