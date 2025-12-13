This is a single, copy‑paste‑ready README you can drop into `README.md`.

```markdown
# Healthcare Backend – Django + DRF

## Overview
This project is a backend system for a healthcare application built with Django, Django REST Framework (DRF), and PostgreSQL. It provides APIs for user registration/login, managing patients and doctors, and assigning doctors to patients using secure JWT-based authentication.

## Features
- User registration and JWT authentication
- CRUD operations for Patients and Doctors
- Assign multiple Doctors to a Patient (patient–doctor mappings)
- Auth-protected endpoints using Bearer token
- PostgreSQL database with Django ORM
- `.env`-based configuration for secrets and DB settings
- VSCode REST Client test suite (`tests.rest`)

## Tech Stack
- Python 3.x  
- Django 4.x  
- Django REST Framework  
- djangorestframework-simplejwt  
- PostgreSQL  
- python-dotenv (or python-decouple) for environment variables  
- VSCode REST Client (optional, for testing)

## Setup & Installation

1. **Clone the repository**
   ```
   git clone <repo_url>
   cd healthcare_backend
   ```

2. **Create and activate virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```
   SECRET_KEY=<your_django_secret_key>
   DEBUG=True
   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=<your_password>
   DB_HOST=localhost
   DB_PORT=5432
   ```

   Ensure `.env` is listed in `.gitignore` so secrets are not committed.

5. **Apply migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` – Register a new user  
- `POST /api/auth/login/` – Obtain JWT access/refresh tokens  

### Patients
- `POST /api/patients/` – Create patient (auth required)  
- `GET /api/patients/` – List patients for logged-in user (auth)  
- `GET /api/patients/<id>/` – Retrieve single patient (auth)  
- `PUT /api/patients/<id>/` – Update patient (auth)  
- `DELETE /api/patients/<id>/` – Delete patient (auth)  

### Doctors
- `POST /api/doctors/` – Create doctor (auth)  
- `GET /api/doctors/` – List all doctors (auth)  
- `GET /api/doctors/<id>/` – Retrieve single doctor (auth)  
- `PUT /api/doctors/<id>/` – Update doctor (auth)  
- `DELETE /api/doctors/<id>/` – Delete doctor (auth)  

### Patient–Doctor Mappings
- `POST /api/mappings/` – Assign doctor to patient (auth)  
- `GET /api/mappings/` – List all mappings (auth)  
- `GET /api/mappings/<patient_id>/` – Get all doctors for a patient (auth)  
- `DELETE /api/mappings/<id>/` – Remove a doctor from a patient (auth)  

## Testing

### VSCode REST Client

A `tests.rest` (or `tests.http`) file contains a full suite of requests for this API.

Usage:
1. Install the **REST Client** extension in VSCode.  
2. Open `tests.rest`.  
3. Click `Send Request` above any request to execute it.  
4. After calling the login endpoint, copy the `access` token from the JSON response and replace the `{{ACCESS_TOKEN}}` placeholder (or `<ACCESS_TOKEN>` if you use that style) in subsequent protected requests.

### Manual Testing (Postman / curl)

For protected endpoints add:

- Header: `Authorization: Bearer <ACCESS_TOKEN>`  
- Header: `Content-Type: application/json` for POST/PUT requests  

## Admin Panel
Access the Django admin at:

```
http://127.0.0.1:8000/admin/
```

Login with the superuser to manage Users, Patients, Doctors, and Mappings through the web interface.

## Notes
- Sensitive settings (SECRET_KEY, DB credentials, DEBUG) are loaded from `.env`.  
- Patient-related endpoints are scoped to the authenticated user.  
- JWT tokens are required for protected endpoints; expired or invalid tokens return `401 Unauthorized`.  

## License
This project is intended for learning and demonstration purposes.
```