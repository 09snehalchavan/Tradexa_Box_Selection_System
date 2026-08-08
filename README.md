# AI-Assisted Box Selection System

## Overview

A Django REST Framework based box selection system that recommends
a suitable shipping box based on product dimensions, weight,
available box capacity, and box cost.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Django ORM
- Django Admin
- REST API

## Features

- Manage shipping boxes through Django Admin
- Manage products
- Manage orders
- List available boxes through REST API
- Recommend a suitable box through REST API
- Store recommended box and order details
- Retrieve order history
- Validate product dimensions and weight
- Automated API test cases

## Project Structure

```text
Tradexa_Box_Selection_System/
│
├── config/
├── shipping/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── TEST_OUTPUT.md
```

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create admin user

```bash
python manage.py createsuperuser
```

### 6. Run development server

```bash
python manage.py runserver
```

## Admin Panel

Open:

```text
http://127.0.0.1:8000/admin/
```

The admin panel can be used to manage:

- Boxes
- Products
- Orders

## API Endpoints

### Get Available Boxes

```text
GET /api/boxes/
```

### Recommend a Box

```text
POST /api/recommend-box/
```

Example request:

```json
{
    "products": [
        {
            "name": "Laptop",
            "length": 30,
            "width": 20,
            "height": 5,
            "weight": 2
        }
    ]
}
```

Example response:

```json
{
    "order_id": 1,
    "recommended_box": "Small Box",
    "cost": "40.00"
}
```

### Get Orders

```text
GET /api/orders/
```

## Testing

Run the automated tests:

```bash
python manage.py test shipping
```

The current test suite contains 3 tests and all tests pass successfully.

See `TEST_OUTPUT.md` for the test run output.

## AI Usage

AI assistance was used during development for learning,
implementation guidance, debugging, and documentation support.

See `AI_USAGE.md` for details.

## Project Verification

The project was verified using:

- Django system checks
- Database migrations
- Django Admin
- REST API requests
- Automated tests

## What I Learned

### 1. Django

* I understood the Django project structure.
* I learned how to connect the model, URL, and view files with each other.

### 2. Box Selection Logic

* I learned how to compare product dimensions and weight with the box dimensions and weight capacity.
* I understood what makes a box suitable for an order.

### 3. API

* I understood the flow from creating an order to getting the box recommendation.
* I learned how to structure API requests and responses.

### 4. Testing

* I learned how to test different cases and verify whether the box selection logic works correctly.
* I understood the importance of testing different conditions and possible failures.
