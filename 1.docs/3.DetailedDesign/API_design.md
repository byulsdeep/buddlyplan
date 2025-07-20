## Event Horizon - API Endpoint Design

### **Common Conventions**

*   **Base URL:** All endpoints are prefixed with `/api/v1`.
*   **Authentication:** All protected endpoints must include an `Authorization: Bearer <ACCESS_TOKEN>` header. A `401 Unauthorized` response will be returned if the token is missing or invalid. A `403 Forbidden` response will be returned if the user is authenticated but not permitted to perform the action.
*   **Data Format:** All request and response bodies are in JSON.
*   **Pagination:** Endpoints that return lists will use `skip` (offset) and `limit` query parameters for pagination (e.g., `GET /posts?skip=0&limit=20`).

---

### 1. Authentication (`/auth`)

These endpoints are public and manage user identity.

*   **`POST /auth/register`**
    *   **Purpose:** Create a new user account.
    *   **Request Body:** `{ "username": "...", "email": "...", "password": "..." }`
    *   **Response (201 Created):** `{ "user": { ...user_object... }, "access_token": "...", "refresh_token": "..." }`

*   **`POST /auth/token`**
    *   **Purpose:** Log a user in by exchanging credentials for tokens.
    *   **Request Body (form-data):** `username=<USERNAME>&password=<PASSWORD>` (This follows the OAuth2 standard `password` flow).
    *   **Response (200 OK):** `{ "access_token": "...", "refresh_token": "...", "token_type": "bearer" }`

*   **`POST /auth/refresh`**
    *   **Purpose:** Obtain a new access token using a valid refresh token.
    *   **Request Body:** `{ "refresh_token": "..." }`
    *   **Response (200 OK):** `{ "access_token": "...", "token_type": "bearer" }`

---

### 2. Users & Friendships (`/users`, `/friends`)

Manage user profiles and relationships. (Protected)

*   **`GET /users/me`**
    *   **Purpose:** Get the complete profile of the currently authenticated user.
    *   **Response (200 OK):** `{ ...full_user_object... }`

*   **`GET /users/me/friends`**
    *   **Purpose:** Get a list of the current user's accepted friends.
    *   **Response (200 OK):** `[ { ...user_summary_object... }, ... ]`

*   **`GET /friends/requests`**
    *   **Purpose:** Get a list of pending incoming friend requests for the current user.
    *   **Response (200 OK):** `[ { "from_user": { ...user_summary_object... }, "sent_at": "..." }, ... ]`

*   **`POST /friends/requests`**
    *   **Purpose:** Send a friend request to another user.
    *   **Request Body:** `{ "user_id": <target_user_id> }`
    *   **Response (202 Accepted):** `{ "status": "pending" }`

*   **`PUT /friends/requests/{requester_id}`**
    *   **Purpose:** Accept or decline a friend request from a specific user.
    *   **Request Body:** `{ "action": "accept" | "decline" }`
    *   **Response (200 OK):** `{ "status": "accepted" | "declined" }`

*   **`DELETE /friends/{user_id}`**
    *   **Purpose:** Unfriend a user.
    *   **Response (204 No Content):**

---

### 3. Posts, Notes & Comments (`/posts`)

The core content engine. (Protected)

*   **`GET /posts`**
    *   **Purpose:** Get the main feed of posts from the user and their friends.
    *   **Query Params:** `?skip=0&limit=20`
    *   **Response (200 OK):** `[ { ...post_object_with_author... }, ... ]`

*   **`GET /users/me/notes`**
    *   **Purpose:** A dedicated endpoint to get the current user's private notes (`is_private=true`).
    *   **Query Params:** `?skip=0&limit=50`
    *   **Response (200 OK):** `[ { ...post_object... }, ... ]`

*   **`POST /posts`**
    *   **Purpose:** Create a new top-level post or a private note.
    *   **Request Body:** `{ "content": "<WYSIWYG_HTML>", "is_private": boolean, "attachments": [ ...file_ids... ] }`
    *   **Response (201 Created):** `{ ...new_post_object... }`

*   **`POST /posts/{post_id}/comments`**
    *   **Purpose:** Add a comment to a post.
    *   **Request Body:** `{ "content": "<WYSIWYG_HTML>" }`
    *   **Response (201 Created):** `{ ...new_comment_object... }`

*   **`GET /posts/{post_id}/comments`**
    *   **Purpose:** Get all comments for a specific post.
    *   **Response (200 OK):** `[ { ...comment_object_with_author... }, ... ]`

*   **`DELETE /posts/{post_id}`**
    *   **Purpose:** Delete a post or comment. (Backend must verify ownership).
    *   **Response (204 No Content):**

---

### 4. Events (`/events`)

Scheduling and calendar functionality. (Protected)

*   **`GET /events`**
    *   **Purpose:** Get all events for the current user within a date range.
    *   **Query Params:** `?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
    *   **Response (200 OK):** `[ { ...event_object... }, ... ]`

*   **`POST /events`**
    *   **Purpose:** Create a new event.
    *   **Request Body:** `{ "title": "...", "description": "...", "start_time": "...", "end_time": "...", "invitees": [ <user_id_1>, <user_id_2> ] }`
    *   **Response (201 Created):** `{ ...new_event_object... }`

*   **`PUT /events/{event_id}/rsvp`**
    *   **Purpose:** Respond to an event invitation.
    *   **Request Body:** `{ "status": "attending" | "maybe" | "declined" }`
    *   **Response (200 OK):** `{ "event_id": ..., "user_id": "me", "status": "..." }`

---

### 5. Real-Time Chat (`/chats` & WebSocket)

Messaging functionality is a hybrid of REST for setup and WebSockets for real-time. (Protected)

#### REST Endpoints

*   **`GET /chats`**
    *   **Purpose:** Get the list of all chat sessions (DMs and groups) for the current user, along with the last message for display.
    *   **Response (200 OK):** `[ { "id": ..., "chat_name": "...", "participants": [...], "last_message": { ... } }, ... ]`

*   **`POST /chats`**
    *   **Purpose:** Create a new chat session.
    *   **Request Body:** `{ "type": "direct" | "group", "participants": [ <user_id_1>, ... ], "chat_name": "..." (if group) }`
    *   **Response (201 Created):** `{ ...new_chat_object... }`

*   **`GET /chats/{chat_id}/messages`**
    *   **Purpose:** Get the message history for a specific chat room.
    *   **Query Params:** `?skip=0&limit=50`
    *   **Response (200 OK):** `[ { ...message_object... }, ... ]`

#### WebSocket Endpoint

*   **`WS /ws/chat/{chat_id}`**
    *   **Purpose:** Establish a persistent, real-time connection to a chat room after authenticating with a JWT.
    *   **Client-to-Server Messages:**
        *   `{ "type": "new_message", "content": "..." }`
        *   `{ "type": "start_typing" }`
        *   `{ "type": "stop_typing" }`
        *   `{ "type": "read_receipt", "last_message_id": ... }`
    *   **Server-to-Client Messages:**
        *   `{ "type": "message_broadcast", "message": { ...full_message_object... } }`
        *   `{ "type": "user_typing", "user": { ...user_summary... } }`
        *   `{ "type": "user_stopped_typing", "user": { ...user_summary... } }`
