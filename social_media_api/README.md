# Social Media API

This project is a Django-based social media API that includes functionalities for user registration, authentication, creating and managing posts and comments, following/unfollowing users, generating a personalized user feed, and implementing notifications and likes functionality.

## Table of Contents
- [Task 0: Setup](#task-0-setup)
- [Task 1: Posts and Comments API](#task-1-posts-and-comments-api)
  - [Posts Endpoint](#posts-endpoint)
  - [Comments Endpoint](#comments-endpoint)
- [Task 2: Follow & Feed API](#task-2-follow--feed-api)
  - [Follow a User](#follow-a-user)
  - [Unfollow a User](#unfollow-a-user)
  - [User Feed](#user-feed)
- [Task 3: Notifications and Likes API](#task-3-notifications-and-likes-api)
  - [Like a Post](#like-a-post)
  - [Unlike a Post](#unlike-a-post)
  - [View Notifications](#view-notifications)
- [Project Setup](#project-setup)

---

## Task 0: Setup

(Setup instructions from Task 0 remain unchanged)

---

## Task 1: Posts and Comments API

(Documentation for Task 1 remains unchanged)

---

## Task 2: Follow & Feed API

(Documentation for Task 2 remains unchanged)

---

## Task 3: Notifications and Likes API

### Like a Post

- **Endpoint**: `/api/posts/<int:pk>/like/`
- **Method**: `POST`
- **Description**: Allows the current authenticated user to like a post.
- **Permissions**: Only authenticated users can like posts.

#### Request Example
```bash
POST /api/posts/1/like/
Authorization: Token <your_token>
```

#### Response Example (Success)
```json
{
  "message": "Post liked successfully"
}
```

#### Response Example (Already Liked)
```json
{
  "error": "You have already liked this post"
}
```

### Unlike a Post

- **Endpoint**: `/api/posts/<int:pk>/unlike/`
- **Method**: `POST`
- **Description**: Allows the current authenticated user to unlike a post they have previously liked.
- **Permissions**: Only authenticated users can unlike posts.

#### Request Example
```bash
POST /api/posts/1/unlike/
Authorization: Token <your_token>
```

#### Response Example (Success)
```json
{
  "message": "Post unliked successfully"
}
```

#### Response Example (Not Liked Yet)
```json
{
  "error": "You have not liked this post yet"
}
```

### View Notifications

- **Endpoint**: `/api/notifications/`
- **Method**: `GET`
- **Description**: Allows the current authenticated user to view their notifications, showing unread notifications prominently.
- **Permissions**: Only authenticated users can view notifications.

#### Request Example
```bash
GET /api/notifications/
Authorization: Token <your_token>
```

#### Response Example (Unread Notifications)
```json
[
  {
    "id": 1,
    "recipient": "john_doe",
    "actor": "jane_doe",
    "verb": "liked your post",
    "target": "Post 1",
    "timestamp": "2024-09-22T10:00:00Z",
    "read": false
  }
]
```

#### Response Example (Read Notifications)
```json
[
  {
    "id": 2,
    "recipient": "john_doe",
    "actor": "jane_doe",
    "verb": "started following you",
    "target": null,
    "timestamp": "2024-09-22T09:45:00Z",
    "read": true
  }
]
```

### Notification Triggers
Notifications are generated for the following actions:
- A user likes your post.
- A user comments on your post.
- A user starts following you.

---

## Project Setup

(Setup instructions remain unchanged)
