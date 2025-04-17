# 🎓 EduNext - E-Learning Microservice Platform

EduNext is a modern e-learning platform designed to deliver interactive, modular education via a microservices architecture. It includes support for video courses, quizzes, user progress tracking, and authentication.

---

## 🚀 Tech Stack

### Backend
- Spring Boot 3 (Java 17+)
- Spring Security (JWT)
- RESTful API
- Eureka Discovery Service
- Spring Cloud Gateway
- MySQL
- Maven

### Frontend
- Angular 16
- SCSS styling
- PDF.js for PDF viewing
- ApexCharts (optional for analytics)
- JWT handling with localStorage

---

## 🧩 Microservices Structure

| Service           | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `user-service`    | Handles authentication, user roles (`ADMIN`, `LEARNER`, `TEACHER`), and profile management |
| `courses-service` | Manages course creation, categories, thumbnails, progress tracking, and recommendations |
| `exams-service`   | Handles exam creation, assignment to users, and submission grading          |
| `forum-service`   | Provides Q&A threads, discussions, and user community features              |
| `live-sessions`   | Manages scheduling, joining, and replaying live video learning sessions     |
| `marketplace`     | Enables users to buy/sell educational content (notes, templates, tools)     |
| `api-gateway`     | Central entry point that routes requests to appropriate microservices       |
| `eureka-server`   | Service registry for discovery and load balancing between microservices     |


---

## 🔐 Authentication

- JWT-based token system
- Role-based access (`ADMIN`, `LEARNER`, `TEACHER`)
- Angular stores token in `localStorage`

---

## 📦 Features

- ✅ Course creation with thumbnail uploads (handled via multipart/form-data)
- ✅ Categorized courses with pack types & levels
- ✅ Search & filter courses by name, category, level, likes
- ✅ Vote (like/dislike) courses
- ✅ Trending and recommended courses
- ✅ Auto YouTube recommendations per course

---

## 🧪 API Testing (Postman)

You can test the backend APIs using Postman:
- `POST /api/courses/create` – create new course
- `GET /api/courses/search/by-name?name=java`
- `POST /api/courses/{id}/vote?vote=like`
- `GET /api/courses/{id}/popularity` *(custom scoring)*
- `GET /api/quiz/{id}/results`
- `POST /api/auth/authenticate` *(returns JWT)*

---

## ⚙️ Run the Project

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/edunext.git
   cd edunext
