# Social Media API

## Table of Contents
- [Task 0: Setup](#task-0-setup)
- [Task 1: Posts and Comments API](#task-1-posts-and-comments-api)
  - [Step 7: Document API Endpoints](#step-7-document-api-endpoints)
    - [Posts Endpoint](#posts-endpoint)
    - [Comments Endpoint](#comments-endpoint)
- [Project Setup](#project-setup)

---

## Task 0: Setup

### Setup Instructions

1. **Install dependencies:**

   ```bash
   pip install django djangorestframework
   ```

2. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

3. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

### API Endpoints

#### Register

- **URL:** `/api/accounts/register/`
- **Method:** `POST`
- **Example Request Body:**

   ```json
   {
       "username": "newuser",
       "password": "password123",
       "email": "newuser@example.com"
   }
   ```

- **Response:** Returns a token upon successful registration.

#### Login

- **URL:** `/api/accounts/login/`
- **Method:** `POST`
- **Example Request Body:**

   ```json
   {
       "username": "newuser",
       "password": "password123"
   }
   ```

- **Response:** Returns a token and user details upon successful login.

---

## Task 1: Posts and Comments API

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jazaltron10/JangoBlog
   cd jangosocial
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables in the `.env` file** (e.g., database credentials, secret key).

5. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## Step 7: Document API Endpoints

Below are the details on how to interact with the posts and comments endpoints:

### Posts Endpoint

- **Base URL:** `/api/posts/`

| Method | URL         | Description                   | Authentication |
|--------|-------------|-------------------------------|----------------|
| GET    | `/api/posts/`    | List all posts              | Required       |
| POST   | `/api/posts/`    | Create a new post           | Required       |
| GET    | `/api/posts/{id}/` | Retrieve a specific post   | Required       |
| PUT    | `/api/posts/{id}/` | Update an existing post    | Required       |
| DELETE | `/api/posts/{id}/` | Delete a post             | Required       |

#### Example Requests:

1. **GET List of Posts:**

   ```http
   GET /api/posts/
   ```

   **Response:**

   ```json
   [
       {
           "id": 1,
           "title": "First Post",
           "body": "This is the content of the first post.",
           "author": "john_doe",
           "created_at": "2023-09-15T12:34:56Z"
       }
   ]
   ```

2. **POST Create a New Post:**

   ```http
   POST /api/posts/
   ```

   **Request Body:**

   ```json
   {
       "title": "New Post",
       "body": "This is the content of my new post."
   }
   ```

   **Response:**

   ```json
   {
       "id": 2,
       "title": "New Post",
       "body": "This is the content of my new post.",
       "author": "john_doe",
       "created_at": "2023-09-15T12:45:00Z"
   }
   ```

3. **GET Specific Post:**

   ```http
   GET /api/posts/1/
   ```

   **Response:**

   ```json
   {
       "id": 1,
       "title": "First Post",
       "body": "This is the content of the first post.",
       "author": "john_doe",
       "created_at": "2023-09-15T12:34:56Z"
   }
   ```

### Comments Endpoint

- **Base URL:** `/api/comments/`

| Method | URL                 | Description                     | Authentication |
|--------|---------------------|---------------------------------|----------------|
| GET    | `/api/comments/`        | List all comments               | Required       |
| POST   | `/api/comments/`        | Create a new comment            | Required       |
| GET    | `/api/comments/{id}/`   | Retrieve a specific comment     | Required       |
| PUT    | `/api/comments/{id}/`   | Update an existing comment      | Required       |
| DELETE | `/api/comments/{id}/`   | Delete a comment                | Required       |

#### Example Requests:

1. **GET List of Comments:**

   ```http
   GET /api/comments/
   ```

   **Response:**

   ```json
   [
       {
           "id": 1,
           "post": 1,
           "body": "This is the first comment on the first post.",
           "author": "jane_doe",
           "created_at": "2023-09-15T13:00:00Z"
       }
   ]
   ```

2. **POST Create a New Comment:**

   ```http
   POST /api/comments/
   ```

   **Request Body:**

   ```json
   {
       "post": 1,
       "body": "This is a new comment on the first post."
   }
   ```

   **Response:**

   ```json
   {
       "id": 2,
       "post": 1,
       "body": "This is a new comment on the first post.",
       "author": "jane_doe",
       "created_at": "2023-09-15T13:10:00Z"
   }
   ```

3. **GET Specific Comment:**

   ```http
   GET /api/comments/1/
   ```

   **Response:**

   ```json
   {
       "id": 1,
       "post": 1,
       "body": "This is the first comment on the first post.",
       "author": "jane_doe",
       "created_at": "2023-09-15T13:00:00Z"
   }
   ```

---

This README includes **Task 0** for initial setup, as well as **Task 1** documentation for Posts and Comments API.