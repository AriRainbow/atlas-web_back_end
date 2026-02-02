# Basic Authentication

This project implements a basic authentication system for a RESTful API using Flask in Python. It includes route protection, Base64 processing, and user credential validation.

## Files and Directories

- `api/v1/app.py`: Main app entry point. Registers blueprints, CORS, and authentication handlers.
- `api/v1/auth/__init__.py`: Empty file to make the directory a Python package.
- `api/v1/auth/auth.py`: Base `Auth` class with generic authentication methods.
- `api/v1/auth/basic_auth.py`: Extends `Auth` to implement HTTP Basic Authentication.
- `models/user.py`: Contains the `User` model and related methods.
- `main_0.py` to `main_6.py`: Test scripts for verifying functionality of each task.

## Environment Variables

- `API_HOST`: Host IP (default is `0.0.0.0`)
- `API_PORT`: Port number (default is `5000`)
- `AUTH_TYPE`: Determines which authentication class to use (`auth` or `basic_auth`)

## Tasks

### 0. Setup and Requirements
- All files use Python 3.9
- All scripts begin with `#!/usr/bin/env python3`
- `README.md` present at root

---

### 1. Create Route for Unauthorized and Forbidden
- `/api/v1/unauthorized/` returns `{"error": "Unauthorized"}` with status code `401`
- `/api/v1/forbidden/` returns `{"error": "Forbidden"}` with status code `403`

---

### 2. Auth Class Template
- `Auth` class created in `auth.py`
- `require_auth()` returns `False`
- `authorization_header()` returns `None`
- `current_user()` returns `None`

---

### 3. Define Unprotected Routes
- Updated `require_auth(path, excluded_paths)`:
  - Returns `True` if path is None or not excluded
  - Matches path even if missing trailing slash

---

### 4. Request Validation
- Validates all requests using `@app.before_request`
- Aborts with:
  - `401` if no authorization header
  - `403` if user not found
- Skips validation for:
  - `/api/v1/status/`
  - `/api/v1/unauthorized/`
  - `/api/v1/forbidden/`

---

### 5. Authorization Header Logic
- `authorization_header(request)`:
  - Returns `None` if request is `None` or missing `Authorization` header
  - Otherwise returns the header string

---

### 6. BasicAuth Class
- Created `BasicAuth` class inheriting from `Auth`
- Swaps in via `AUTH_TYPE=basic_auth`

---

### 7. Extract Base64 String
- `extract_base64_authorization_header(authorization_header)`:
  - Validates `authorization_header` is a string starting with `"Basic "`
  - Returns the Base64 portion only

---

### 8. Decode Base64 Auth Header
- `decode_base64_authorization_header(base64_str)`:
  - Validates Base64 format
  - Returns decoded string in UTF-8

---

### 9. Extract User Credentials
- `extract_user_credentials(decoded_str)`:
  - Validates string contains `:`
  - Splits string into `(email, password)` tuple

---

### 10. Get User Object
- `user_object_from_credentials(email, password)`:
  - Searches for user via `User.search`
  - Verifies password using `is_valid_password`
  - Returns `User` instance or `None`

---

### 11. current_user()
- Overrides `current_user(request)` in `BasicAuth`
- Chain of auth steps:
  - `authorization_header()`
  - `extract_base64_authorization_header()`
  - `decode_base64_authorization_header()`
  - `extract_user_credentials()`
  - `user_object_from_credentials()`

---

## Example Usage

Start API:
```bash
AUTH_TYPE=basic_auth API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app