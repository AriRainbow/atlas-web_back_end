# Personal Data

This project focuses on protecting **Personally Identifiable Information (PII)** in backend systems using Python. It covers best practices for filtering, logging, and securing sensitive data such as emails, passwords, and Social Security Numbers (SSNs).

## Learning Objectives

By the end of this project, you will be able to:

- Identify examples of PII (e.g., name, email, SSN, phone number, password)
- Implement a log filter that obfuscates PII fields using regular expressions
- Encrypt and validate passwords securely using the `bcrypt` module
- Connect to a MySQL database using credentials stored as environment variables
- Apply logging best practices to avoid leaking sensitive data

## Technologies Used

- Python 3.9
- Ubuntu 20.04
- `bcrypt` for password hashing
- `mysql-connector-python` for database connections
- `re`, `logging`, `os` modules
- `pycodestyle` (version 2.5)

## Files

| File | Description |
|------|-------------|
| `filtered_logger.py` | Contains functions and classes to filter PII, configure loggers, connect to MySQL, and redact data when reading from a user database. |
| `encrypt_password.py` | Contains functions to securely hash and validate passwords using bcrypt. |
| `user_data.csv` | Sample data file (not included in repo) to simulate realistic logging and filtering scenarios. |
| `main.py` | Test files for each task (used during development and grading). |

## Environment Variables

The following environment variables are used to connect to the MySQL database:

- `PERSONAL_DATA_DB_USERNAME` (default: `"root"`)
- `PERSONAL_DATA_DB_PASSWORD` (default: `""`)
- `PERSONAL_DATA_DB_HOST` (default: `"localhost"`)
- `PERSONAL_DATA_DB_NAME` (**required**)

## Usage

```bash
PERSONAL_DATA_DB_USERNAME=root \
PERSONAL_DATA_DB_PASSWORD=yourpassword \
PERSONAL_DATA_DB_HOST=localhost \
PERSONAL_DATA_DB_NAME=my_db \
./filtered_logger.py