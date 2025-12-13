# Healthcare Backend - Django Project

## Overview

This project is a **backend system for a healthcare application** built using Django, Django REST Framework (DRF), and PostgreSQL. It allows users to register, log in, and manage patients, doctors, and patient-doctor assignments securely.

## Features

* User Registration and JWT Authentication
* CRUD for Patients and Doctors
* Assign Doctors to Patients (Mapping)
* Secure APIs with token-based authorization
* PostgreSQL database integration

## Technologies Used

* Python 3.x
* Django 4.x
* Django REST Framework
* djangorestframework-simplejwt (JWT Authentication)
* PostgreSQL

## Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd healthcare_backend
```

2. Create virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure `settings.py` with your PostgreSQL credentials.
5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:

```bash
python manage.py createsuperuser
```

7. Run the server:

```bash
python manage.py runserver
```

## API Endpoints

* **Authentication**

  * POST `/api/auth/register/` - Register a new user
  * POST `/api/auth/login/` - Login and get JWT token
* **Patients**

  * POST `/api/patients/` - Add patient
  * GET `/api/patients/` - List patients
  * GET `/api/patients/<id>/` - Get patient
  * PUT `/api/patients/<id>/` - Update patient
  * DELETE `/api/patients/<id>/` - Delete patient
* **Doctors**

  * POST `/api/doctors/` - Add doctor
  * GET `/api/doctors/` - List doctors
  * GET `/api/doctors/<id>/` - Get doctor
  * PUT `/api/doctors/<id>/` - Update doctor
  * DELETE `/api/doctors/<id>/` - Delete doctor
* **Mappings**

  * POST `/api/mappings/` - Assign doctor to patient
  * GET `/api/mappings/` - List all mappings
  * GET `/api/mappings/<patient_id>/` - Get mappings for a patient
  * DELETE `/api/mappings/<id>/` - Remove a doctor from a patient

## Testing

Use Postman to test APIs. Set **Authorization → Bearer Token** with the JWT access token received from login.

## Admin Panel

Access Django admin at:

```
http://127.0.0.1:8000/admin/
```

Manage Users, Patients, Doctors, and Mappings from the admin interface.

## Notes

* The `user` field in patients and mappings is automatically set from the logged-in user.
* JWT token is required for all protected endpoints.

## License

This project is for educational purposes.
