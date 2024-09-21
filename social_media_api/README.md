# Social Media API

## TASK 0
### Setup
1. Install dependencies:
    ```
    pip install django djangorestframework
    ```

2. Run migrations:
    ```
    python manage.py migrate
    ```

3. Start the server:
    ```
    python manage.py runserver
    ```

### API Endpoints

#### Register
- URL: `/api/accounts/register/`
- Method: `POST`
- Example Request Body:
    ```json
    {
        "username": "newuser",
        "password": "password123",
        "email": "newuser@example.com"
    }
    ```
- Response: Returns a token on successful registration.

#### Login
- URL: `/api/accounts/login/`
- Method: `POST`
- Example Request Body:
    ```json
    {
        "username": "newuser",
        "password": "password123"
    }
    ```
- Response: Returns a token and user details on successful login.
