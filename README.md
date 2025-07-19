# Event Horizon

## Overview

Event Horizon is a personal SNS and scheduling app that combines social networking features with a calendar scheduler supporting event sharing and Google Calendar sync. Designed for personal use and skill-building.

---

## Features

### Social Networking (SNS)
- User authentication (email/password, social login)  
- User account management and settings  
- Follow system  
- Timeline/feed with privacy controls (private, followers-only, public)  
- Media albums  
- Direct messaging and group chat  
- User blocking  
- Search (users, posts, tags, keywords)  
- Notifications (friend requests, messages, post interactions)  

### Scheduling
- Monthly calendar view  
- Event creation, editing, deletion  
- Event sharing (private, followers, public)  
- Google Calendar sync  
- Event notifications and reminders  

---

## Tech Stack

- Frontend: React  
- Backend: FastAPI  
- Database: PostgreSQL  
- Containerization: Docker  
- Caching: Redis  
- CI/CD: AWS CodePipeline  
- Hosting: AWS EC2 + ELB  
- Secrets: AWS Secrets Manager  
- Monitoring: AWS CloudWatch  

---

## Setup

### Prerequisites

- Node.js  
- Python 3.9+  
- Docker & Docker Compose  
- AWS Account  

### Installation

```bash
git clone https://github.com/byulsdeep/event-horizon.git
cd event-horizon
docker-compose up --build
```

---

## Project Structure

```
/backend      # FastAPI backend  
/frontend     # React frontend  
/docker       # Docker configs  
/docs         # Documentation  
```

---

## Roadmap

- User authentication & authorization  
- SNS core features  
- Messaging & group chat  
- Scheduler & Google Calendar integration  
- Notifications  
- AWS deployment & CI/CD  
- Future: voice/video calls, media albums  

---

## Contributing

Open issues or pull requests are welcome.

---

## License

MIT © 2025 Event Horizon

---

## Contact

byulzdeep@gmail.com
