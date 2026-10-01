# API Testing Automation

This project demonstrates automated REST API testing with Python, Requests, and Pytest against JSONPlaceholder's public mock API.

## Coverage

- GET collection validation
- POST response validation
- PUT response validation
- DELETE status validation
- Explicit request timeouts to prevent hanging test runs
- Automated tests on Python 3.11 and 3.12

## Setup

Python 3.11 or newer is recommended.

```bash
python -m pip install -r requirements.txt
```

## Run tests

```bash
pytest -q
```

The tests require internet access and depend on the availability of `jsonplaceholder.typicode.com`; they do not modify persistent remote data.
