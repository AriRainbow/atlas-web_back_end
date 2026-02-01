# Personal Data

This project demonstrates how to protect Personally Identifiable Information (PII) in backend systems using Python. It includes secure logging, database access, and password hashing.

## Features

- Redacts sensitive fields (like name, email, ssn, password) from log output
- Connects securely to a MySQL database using environment variables
- Uses a custom log formatter to prevent PII leaks
- Hashes passwords securely using bcrypt
- Verifies password input against hashed values

## Technologies

- Python 3.9
- MySQL (via `mysql-connector-python`)
- `bcrypt` for password hashing
- `re` and `logging` for filtering and structured logs
- Compliant with `pycodestyle` 2.5

## Setup & Usage

Set your environment variables and run the logger:

```bash
PERSONAL_DATA_DB_USERNAME=root \
PERSONAL_DATA_DB_PASSWORD=root \
PERSONAL_DATA_DB_HOST=localhost \
PERSONAL_DATA_DB_NAME=my_db \
./filtered_logger.py
```