# EduNext - E-Learning Platform

## 📖 Overview

**EduNext** is a full-featured E-Learning platform that offers a modern and interactive educational experience. Designed and developed by a team of 6 dedicated developers, the application provides personalized learning journeys for students, powerful tools for teachers, and administrative control for platform governance.

Key features include course and quiz management, live virtual classrooms, gamified learning, certification issuance, forums, blog content, and a marketplace for educational resources. The platform is built with robust authentication (JWT, 2FA), role-based access control, and clean API design following REST principles.

- **Backend:** Spring Boot 3 & Spring Security 6  
- **Frontend:** Angular with TailwindCSS  
- **Database:** PostgreSQL / MongoDB  
- **Security:** JWT, HTTPS, OAuth2, Role-based Access  
- **Documentation:** Swagger & OpenAPI  
- **Deployment:** Dockerized, GitHub Actions CI/CD

---

## ✨ Features

### 👥 User Management
- Sign up via email or social login
- Secure login with 2FA
- Role-based access (Student, Teacher, Admin)
- Profile management & activity tracking

### 📚 Courses & Quizzes
- Enroll in multimedia courses (videos, documents)
- Intelligent course recommendations
- Take quizzes (MCQs, true/false, short answers)
- Real-time feedback and progress tracking

### 🎓 Exams & Certifications
- Secure online exams (browser lockdown, timers, proctoring)
- Automatic grading & behavior monitoring
- Issue and manage verifiable digital certificates

### 🕹️ Gamification & Community
- Complete challenges and earn badges or EduCoins
- Participate in forums and blogs
- AI-powered suggestions for content and discussions
- Discover and join educational events

### 📹 Virtual Classrooms & Mentoring
- Live session scheduling with calendar integration
- Mentorship programs with one-on-one booking
- Smart assistant support and learning recommendations

### 🛒 Marketplace & Donations
- Buy or sell educational content
- Launch and support crowdfunding campaigns
- Secure payment integration
- Track donations and campaign outcomes

---

## 🔧 Technologies Used

### Backend (`edunext-backend`)
- Spring Boot 3
- Spring Security 6
- JWT Token Authentication
- Spring Data JPA
- JSR-303 & Spring Validation
- Swagger & OpenAPI
- Docker
- GitHub Actions
- PostgreSQL / MongoDB
- Keycloak (for OAuth2 and Identity Management)

### Frontend (`edunext-ui`)
- Angular
- TailwindCSS
- Lazy Loading
- Component-based Architecture
- Route Guards & Auth Interceptor
- OpenAPI Generator for Angular
- Framer Motion (animations)
- Responsive UI Design

---

## 🎯 Learning Objectives

This project offers a rich learning experience in both frontend and backend development, including:

- Designing software architecture and modular monorepos
- Building secure login systems with JWT and Spring Security
- Email-based account activation and validation
- JPA with inheritance and complex relationships
- Pagination, exception handling & API best practices
- Environment-based configuration via Spring Profiles
- API documentation using Swagger/OpenAPI
- Docker-based infrastructure setup
- Building and deploying CI/CD pipelines
- Integrating AI-powered assistants
- Managing real-time features and live sessions

---

## 🧪 Getting Started

To get started with EduNext, follow the setup instructions in the appropriate directories:

- [`backend/README.md`](./backend/README.md)
- [`frontend/README.md`](./frontend/README.md)

---

## 📜 License

This project is licensed under the **Apache License 2.0**.  
See the [LICENSE](./LICENSE) file for full details.

---

## 👥 Contributors

- **EduNext Development Team** (6 members)
  - Backend & Security
  - Frontend UI/UX
  - DevOps & Infrastructure
  - QA & Testing
  - AI & Recommendation Systems
  - Content & Community Features

---

## 🙏 Acknowledgments

Special thanks to the developers, open-source contributors, and maintainers of the tools and technologies that powered EduNext. Your innovation makes impactful projects like this possible.

---

*Empowering education through technology. Learn, teach, and grow with EduNext.*
