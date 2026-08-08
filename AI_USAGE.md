# AI Usage

## AI Tool Used

ChatGPT

## Purpose of AI Assistance

AI assistance was used during development for:

- Understanding Django project setup
- Understanding Django models and relationships
- Django REST Framework implementation guidance
- Serializer and API development
- Recommendation logic discussion
- Debugging development issues
- Writing and organizing project documentation
- Designing automated test cases

## Prompts / Questions Used

Examples of questions asked during development:

1. How should the Django project and shipping app be structured?
2. How should Box, Product, and Order models be designed?
3. How should Django REST Framework serializers be implemented?
4. How should the box recommendation logic be structured?
5. How should the REST API endpoints be created?
6. How can the API implementation be tested?
7. How should the project README and test output documentation be organized?

## Accepted Outputs

AI suggestions were accepted when they matched the assignment requirements
and the project's implementation approach.

The generated code was manually reviewed and tested before being retained.

## Modified or Rejected Outputs

Suggestions were modified whenever they did not exactly match the project's
requirements, existing project structure, or implementation decisions.

AI-generated suggestions were not copied blindly.

## Mistakes Identified

During development, implementation suggestions and code were checked for:

- Correct Django model relationships
- Correct API routing
- Serializer behavior
- Recommendation logic
- Database persistence
- API response status codes
- Automated test results

## Verification Steps

The implementation was verified using:

### Django System Check

```bash
py manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

### Database Migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

The migrations completed successfully.

### Django Admin

Boxes, Products, and Orders were verified through the Django Admin panel.

### API Verification

The following APIs were tested:

```text
GET /api/boxes/
POST /api/recommend-box/
GET /api/orders/
```

The recommendation API successfully created an order and stored the
recommended box.

### Automated Tests

```bash
py manage.py test shipping
```

Result:

```text
Ran 3 tests

OK
```

The test output is documented in `TEST_OUTPUT.md`.

## Final Verification

AI-generated suggestions were verified by running the project locally,
checking the Django Admin panel, testing REST API endpoints, and running
automated tests.