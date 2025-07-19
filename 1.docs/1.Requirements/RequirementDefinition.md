# Project: Event Horizon - Requirements Definition

**Version:** 1.0
**Date:** July 22, 2025
**Author:** Byul

## 1. Introduction & Vision

### 1.1. Project Vision
Event Horizon is a cross-platform application designed for a private circle of friends and family. It merges a social network (SNS), a private note-taking system, and a collaborative scheduling tool into a single, cohesive experience. The core philosophical theme is the passionate pursuit of knowledge and understanding, embodied by a unique feature: interactive AI personas of historical figures who engage with users.

The name "Event Horizon" reflects the app's dual nature: managing life's "events" on the horizon of one's schedule, while philosophically exploring the "event horizon" of knowledge—the boundary of what is known and what remains a mystery.

### 1.2. Target Audience
-   Primary: The developer and a small, private group of family and friends.
-   Secondary: Potential employers viewing this as a portfolio project demonstrating a wide range of full-stack development skills.

### 1.3. Core Goals
-   To serve as a practical, personal tool for note-taking, scheduling, and private communication.
-   To strengthen and showcase advanced software development skills across the full stack.
-   To create a unique and engaging user experience through AI integration.

## 2. Functional Requirements (User Stories)

### 2.1. User & Identity Management
-   As a new user, I can register for an account using an email and password.
-   As a user, I can log in and log out securely.
-   As a user, I can view and edit my profile (username, display name, profile picture).
-   As a user, I can navigate to a dedicated **Settings Page** to manage my account, privacy settings, and notification preferences.

### 2.2. Social Network & Notes System (WYSIWYG Editor)
-   As a user, I can view a central "feed" containing posts from myself and my friends, sorted chronologically.
-   As a user, I can create, read, update, and delete a post using a **WYSIWYG (What You See Is What You Get) editor**.
-   The editor must support rich text formatting, image/file uploads, and embedding video links (e.g., from YouTube) which render as an iframe.
-   **Image and file uploads** must be stored securely in **AWS S3**.
-   As a user, I can mark a post as "Private," making it visible only to me. These private posts constitute the "Notes" feature.
-   As a user, I can comment on any post visible to me.

### 2.3. Real-Time Chat & Messaging
-   As a user, I can initiate a **one-on-one real-time chat** with a friend.
-   As a user, I can create **group chats** by inviting multiple friends.
-   The chat interface must show real-time typing indicators and read receipts.
-   Chat history must be persistent and scrollable.

### 2.4. Scheduling & Events System
-   As a user, I can navigate to a dedicated "Calendar" section.
-   As a user, I can optionally **synchronize my Google Calendar** (one-way or two-way sync) to view and/or manage events from Event Horizon.
-   As a user, I can create a personal event with a title, description, start/end times, and location.
-   As a user, I can create a group event and invite friends, who can RSVP ("Attending," "Maybe," "Not Attending").
-   As a user, I can set **reminders for events** (e.g., 1 hour before, 1 day before).

### 2.5. AI Persona Integration ("The Echos")
-   As an administrator, I can create "virtual user" accounts for historical figures (e.g., Einstein, Newton), clearly marked as AI.
-   As a user, I can @-mention an AI persona in a post or comment.
-   When an AI is mentioned, the system will query a third-party LLM API with a context-specific prompt. The AI's response will be automatically posted as a comment.
-   As a user, I can have a one-on-one chat with an AI persona, with persistent conversation history.

### 2.6. Search & Discovery
-   As a user, I have access to an **advanced, global search bar**.
-   I can search for users, posts, notes, events, and chat messages.
-   Search results should be relevant and quickly accessible.

### 2.7. Notifications
-   As a user, I want to receive a real-time push notification for:
    -   New friend requests and acceptances.
    -   Comments or mentions in posts.
    -   New direct messages or group chat mentions.
    -   Event invitations and updates.
    -   **Configurable event reminders**.
-   Notifications must be delivered on both Web (Web Push) and Mobile (Native Push) platforms.
-   Notification preferences (e.g., disable certain types) must be manageable in the user Settings Page.

## 3. Non-Functional Requirements

### 3.1. Platform Support & Performance
-   The application must be a responsive Single-Page Application (SPA) functional on modern PC web browsers.
-   The web application will be packaged into native mobile apps for **Android** (Phone & Tablet) and eventually **iOS**.
-   API response times should average under 300ms; time-to-interactive on the frontend should be under 3 seconds.

### 3.2. Security (Precise Definition)
-   **Authentication:** User authentication will be handled using **JSON Web Tokens (JWT)**. A short-lived access token will be used for API requests, and a long-lived refresh token stored securely (e.g., in an HttpOnly cookie) will be used to obtain new access tokens without requiring the user to log in again.
-   **Authorization:** The backend will enforce strict, role-based and ownership-based access control on every API endpoint. A user must not be able to access or modify data that does not belong to them or their group.
-   **Input Validation:** All incoming data from clients (API request bodies, query parameters, headers) will be rigorously validated using **Pydantic models in FastAPI**. This prevents malformed data and is a first-line defense against injection attacks.
-   **SQL Injection:** The use of an ORM (like SQLAlchemy) with parameterized queries is mandatory. Raw SQL queries will be forbidden unless absolutely necessary and heavily scrutinized.
-   **LLM Injection (Prompt Injection):** User-provided input that is passed to LLM APIs will be sanitized. Techniques such as instruction-defense (e.g., "Translate the following text... User input is between <<< and >>>") and output parsing will be implemented to prevent users from hijacking the AI's core instructions.
-   **CORS (Cross-Origin Resource Sharing):** The FastAPI backend will implement a strict CORS policy, allowing requests only from the specific domain(s) of the frontend application. Wildcard origins (`*`) are forbidden in production.
-   **CSRF (Cross-Site Request Forgery):** Since the primary authentication mechanism is JWTs sent in the `Authorization` header, the app is largely protected from traditional CSRF attacks. If any session-based authentication (like for Google OAuth flow) is used, CSRF tokens must be implemented.
-   **Rate Limiting:** The API will implement rate limiting on sensitive endpoints (e.g., login, password reset, message sending) to protect against brute-force attacks and denial-of-service.
-   **Secret Management:** All secrets (database credentials, JWT secret keys, third-party API keys) will be managed via **AWS Secrets Manager** and dynamically loaded by the application at runtime. They will never be stored in source code or environment files.
-   **HTTPS:** All traffic will be encrypted end-to-end using TLS/SSL, enforced by the **AWS Elastic Load Balancer (ELB)**.

### 3.3. Scalability & DevOps
-   The application will be hosted on **AWS**.
-   The backend will be containerized (Docker) and deployed on a scalable service (e.g., AWS ECS or App Runner) behind an **ELB**.
-   The database will be a managed **AWS RDS for PostgreSQL** instance.
-   A **CI/CD pipeline** via **AWS CodePipeline** will automate testing and deployment.
-   Application health, logs, and metrics will be monitored using **AWS CloudWatch**.

## 4. Technology Stack

-   **Backend:** Python 3.11+ with FastAPI.
-   **Database:** PostgreSQL (via AWS RDS).
-   **Real-time Layer:** WebSockets (supported by FastAPI).
-   **Frontend:** React (v18+) with TypeScript, built with Vite.
-   **WYSIWYG Editor:** A library like TipTap or Slate.js.
-   **Mobile Wrapper:** Capacitor.
-   **AI Integration:** A provider-agnostic adapter for LLM APIs.
-   **Infrastructure:** AWS (RDS, S3, ELB, Secrets Manager, CloudWatch, CodePipeline).