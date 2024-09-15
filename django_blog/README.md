# Django Blog Project - Authentication System Documentation

## Objective

This documentation provides a detailed overview of the authentication system implemented in the Django Blog project. It includes instructions on how users can register, log in, log out, and manage their profiles, as well as testing guidelines to ensure the functionality works as expected.

## 1. User Registration

### How to Register:

- Navigate to the registration page by visiting `/register`.
- Fill out the registration form with the following fields:
    - **Username**
    - **Email**
    - **Password** (must be entered twice for confirmation)
- Submit the form to create a new user account.

Once registered, the user is automatically logged in and redirected to the homepage.

### URL for Registration:

```
/register
```

---

## 2. User Login

### How to Log In:

- Navigate to the login page by visiting `/login`.
- Enter the username and password used during registration.
- Submit the form to log in to the blog.

Upon successful login, the user is redirected to the homepage and can now access personalized features such as posting, commenting, and profile management.

### URL for Login:

```
/login
```

---

## 3. User Logout

### How to Log Out:

- While logged in, navigate to the logout page by visiting `/logout`.
- Logging out ends the current session and redirects the user to the homepage.

### URL for Logout:

```
/logout
```

---

## 4. Profile Management

### How to View and Edit Profile:

- After logging in, navigate to the profile page by visiting `/profile`.
- The profile page displays the user’s current information (e.g., username, email).
- To edit profile details:
    - Update the username and email in the provided form fields.
    - Submit the form to save changes.

### Optional Feature:
- Extend the profile management system to include additional fields like a profile picture or bio (not implemented by default).

### URL for Profile Management:

```
/profile
```

---

## 5. Testing Instructions

To ensure the authentication system functions as expected, follow these steps:

### 1. Registration:
- Test registration by visiting the `/register` URL.
- Enter valid details and ensure the user is redirected to the homepage after successful registration.
- Ensure that invalid inputs (e.g., mismatched passwords) show appropriate error messages.

### 2. Login:
- Test login by visiting the `/login` URL.
- Ensure that valid credentials successfully log in the user.
- Test invalid login attempts (e.g., wrong username/password) and verify that error messages are displayed.

### 3. Logout:
- Test logout by visiting the `/logout` URL.
- Ensure that the user is successfully logged out and redirected to the homepage.

### 4. Profile Management:
- Test the profile update by visiting `/profile` while logged in.
- Ensure that the user’s profile details (e.g., username, email) can be updated.
- Ensure that unauthorized users cannot access the profile page.

### Security Testing:
- Verify that CSRF tokens are present in all forms to protect against cross-site request forgery attacks.
- Ensure that passwords are securely hashed by Django’s built-in hashing algorithms.

---

## Summary

This document covers the core functionalities of the authentication system, including user registration, login, logout, and profile management. Detailed instructions are provided for testing each feature to ensure the system operates securely and as expected.

---

## Repository

- **Repo Name:** Alx_DjangoLearnLab
- **Directory:** `django_blog`