# Requirement Definition Document — BuddyPlan

---

## 1. Introduction

- **Purpose:**  
  To define the functional and non-functional requirements for BuddyPlan, a personal SNS and scheduling application.

- **Background:**  
  The owner intends to develop this app both as a skill-building project in web development and as a tool for managing personal schedules and communicating with friends.

- **Scope:**  
  The application is designed for personal use and private sharing among a circle of friends.

---

## 2. Terminology

- **SNS:** Social Networking Service  
- **DM:** Direct Message  
- *(Additional terms to be defined as needed)*

---

## 3. Current Issues / Challenges

- This project involves first-time deployment on AWS, requiring additional research and learning throughout the development process.

---

## 4. Requirements

### 4.1 Functional Requirements

- **SNS Features:**  
  - User authentication (email/password, social login)  
  - User account management and settings  
  - Follow system  
  - Timeline/feed for posts with privacy options (private, followers-only, public)  
  - Media albums  
  - Direct messaging (DM)  
  - Group chat  
  - User blocking functionality  
  - Search capabilities (users, posts, tags, keywords)  
  - Notifications (friend requests, messages, post interactions)

- **Scheduling Features:**  
  - Calendar views (monthly)  
  - Event creation, editing, and deletion  
  - Event sharing options (private, followers, public)  
  - Google Calendar synchronization  
  - Event notifications and reminders

### 4.2 Non-Functional Requirements

- **Performance:**  
  - Fast response times  
  - Support for concurrent users

- **Security:**  
  - Secure authentication and authorization mechanisms (JWT, CSRF protection, CORS policies, HTTPS)  
  - Input validation and rate limiting  
  - Secure HTTP headers  
  - Management of secrets and environment variables  
  - Database security and access control for private data and events

- **Availability:**  
  - High system uptime  
  - Regular backups and disaster recovery plan

- **Other:**  
  - Scalability for future growth  
  - Maintainable and clean codebase

---

## 5. Constraints

- Budget limitations  
- Technical constraints, including AWS deployment experience  
- Deadlines: To Be Determined (TBD)

---

## 6. Assumptions and Environment

- **Hardware:**  
  - Development performed on a personal PC  
  - Deployment hosted on AWS EC2 instances

- **Software:**  
  - Operating System: Linux  
  - Frontend Framework: React  
  - Backend Framework: FastAPI  
  - Database: PostgreSQL  
  - CI/CD Pipeline: AWS CodePipeline  
  - Containerization: Docker  
  - Caching: Redis  
  - Load Balancing: AWS Elastic Load Balancer (ELB)  
  - Secrets Management: AWS Secrets Manager  
  - Logging and Monitoring: AWS CloudWatch

- **Network Environment:**  
  - Internet-based access  
  - Cloud-hosted services infrastructure

---

## 7. Schedule

- Requirement Definition Completion: ASAP  
- Design Completion: TBD  
- Development Start: TBD  
- Testing Period: TBD  
- Planned Release Date: TBD

---

## 8. Additional Notes / Remarks

- Future enhancements may be incorporated after the initial release.  
- Continuous learning and adaptation will be necessary during AWS integration and deployment.
