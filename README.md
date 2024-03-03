[![Web testing](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/alex-wahl/testframework-pytest/actions/workflows/test.yml)

# Test framework with pytest

## Description:

This test framework is a versatile project skeleton that can be used for testing backend systems, frontend applications, and mobile apps. Currently, it supports testing for backend and frontend. 
Support for mobile application testing is planned for future updates.

## Dependencies:

- Python 3.11 and above
- Docker
- Allure
- Pytest
- Selenium
- Poetry

## Installation:

1. Clone the repository to your local machine
2. Install Docker
   3. for mac users: https://docs.docker.com/docker-for-mac/install/
   4. for windows users: https://docs.docker.com/docker-for-windows/install/
   5. for linux users: https://docs.docker.com/desktop/install/linux-install/
3. Install Allure
   4. for mac users: `brew install allure`
   5. for windows users: `scoop install allure`
   6. for linux users: 
      7. `sudo apt-add-repository ppa:qameta/allure`
      8. `sudo apt-get update`
      9. `sudo apt-get install allure`
4. Install Poetry
   5. for mac/linux users: `curl -sSL https://install.python-poetry.org | python3 -`
   6. for windows users: `pip install poetry`

## Setup Project

1. Create a Python virtual environment in the root of the project:

   ```bash
   python3 -m venv venv
   ```

2. Activate the Python virtual environment:
   3. On Mac/Linux:
      4. ```bash
         source venv/bin/activate
         ```
    5. On Windows:
       6. ```bash
          venv\Scripts\activate
          ```
3. Install dependencies:
   ```bash
   poetry install --no-root
   ```
   
## Run Tests Locally

### Run test with PROD environment:
   ```bash
   pytest -s tests/web/ikea/test_ikea.py --env PROD
   ```

### Run only tests tagged with "cookies": 
   ```bash
    pytest -m cookies -s tests/web/ikea/test_ikea.py --env PROD
  ```

## Run Tests in Docker
   ```bash
   docker compose run --rm testframework -s tests/web/ikea/test_ikea.py --env PROD
   ```

## Check Allure reports:

   ```bash
   allure serve allure-results
   ```