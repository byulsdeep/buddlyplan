# Event Horizon

![Event Horizon Banner](https://via.placeholder.com/1280x400/000000/FFFFFF?text=Event+Horizon)

**Event Horizon** is a bespoke, cross-platform social application that merges private notes, group scheduling, and a unique AI-driven chat experience into a single, cohesive universe. It's not just an app; it's a personal space for your thoughts, your plans, and your trusted circle, with a philosophical twist.

This project was born from a desire to build a truly useful personal tool while mastering a modern, full-stack development architecture.

---

## ✨ Core Philosophy

The name "Event Horizon" reflects the app's dual nature:

1.  **Events:** A practical tool for managing life's "events" on the horizon of your schedule, both personal and with friends.
2.  **Horizon of Knowledge:** A philosophical playground for exploring ideas. The app embodies the endless pursuit of understanding, a journey toward a horizon you can approach but never fully reach. This is brought to life by "Echos"—AI personas of historical figures like Einstein and Newton, who interact with users and share their "wisdom" from beyond the event horizon of time.

---

## 🚀 Features

Event Horizon is built on three main pillars:

### 1. Social & Notes (The Personal Log)
*   **Friends-Only Feed:** A private timeline to share moments and thoughts with your inner circle.
*   **WYSIWYG Editor:** Create rich posts with text formatting, image uploads, and embedded video.
*   **Private Notes:** Simply mark a post as "private" to turn it into a personal, searchable note, visible only to you.
*   **Threaded Comments:** Engage in discussions on any post.

### 2. Events & Scheduling (The Shared Timeline)
*   **Personal & Group Events:** Organize your own schedule or plan activities with friends.
*   **RSVP System:** Keep track of who's attending with "Attending," "Maybe," and "Declined" statuses.
*   **Event Reminders:** Get timely push notifications so you never miss an important event.
*   **Google Calendar Sync:** (Planned) Integrate with your existing calendars for a unified view.

### 3. AI & Chat (The Echos)
*   **Real-time Messaging:** Direct and group chats with real-time typing indicators and read receipts.
*   **Interactive AI Personas:** Chat directly with AI "Echos" of historical figures.
*   **AI Mentions:** @-mention an AI like `@Einstein` in a public post to get a context-aware reply, sparking interesting conversations.

---

## 🛠️ Tech Stack & Architecture

This project is a full-stack monorepo demonstrating a modern, scalable, and secure application architecture.

### **Backend**
*   **Framework:** **Python 3.11+** with **FastAPI** for high-performance, async-first API development.
*   **Database:** **PostgreSQL** for its robustness and rich feature set.
*   **Authentication:** **JWT (JSON Web Tokens)** with a secure access/refresh token rotation strategy.
*   **Real-time:** Native **WebSockets** support in FastAPI for chat and live notifications.
*   **ORM:** **SQLAlchemy** (with Alembic for migrations) for safe, modern database interactions.
*   **AI:** A provider-agnostic adapter pattern to integrate with LLMs like GPT or Gemini.

### **Frontend**
*   **Framework:** **React 18** with **TypeScript** for a type-safe, component-based UI.
*   **Build Tool:** **Vite** for a lightning-fast development experience.
*   **State Management:** (e.g., Zustand or Redux Toolkit) for managing complex application state.
*   **Mobile:** **Capacitor** to wrap the web application into a native Android (and future iOS) shell, providing access to native device APIs like Push Notifications.

### **Infrastructure & DevOps (AWS)**
*   **Hosting:** The application is containerized with **Docker** and deployed on **AWS**.
*   **Database:** **AWS RDS for PostgreSQL**.
*   **File Storage:** **AWS S3** for all user-uploaded images and files.
*   **Networking:** **AWS Elastic Load Balancer (ELB)** to manage and distribute traffic.
*   **Security:** **AWS Secrets Manager** for secure handling of all credentials and API keys.
*   **CI/CD:** **AWS CodePipeline** for automated testing and deployment.
*   **Monitoring:** **AWS CloudWatch** for application logging and performance monitoring.

---

## 🖼️ Screenshots

*(This is where you'll put a beautiful screenshot of your app's UI once it's running!)*

![App Screenshot](https://via.placeholder.com/800x600/333333/FFFFFF?text=Event+Horizon+UI+Screenshot)

---

## ⚙️ Getting Started

### Prerequisites
-   Docker & Docker Compose
-   Node.js (v18+)
-   Python (v3.11+)
-   An AWS account (for deployment)

### Installation & Local Development
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/byulsdeep/event-horizon.git
    cd event-horizon
    ```

2.  **Configure Environment Variables:**
    -   Create `.env` files for the backend and frontend based on the `.env.example` templates.
    -   Populate with your local database credentials and other required keys.

3.  **Launch Services with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the application:**
    -   Frontend will be available at `http://localhost:5173` (Vite's default).
    -   Backend API docs will be at `http://localhost:8000/docs`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).