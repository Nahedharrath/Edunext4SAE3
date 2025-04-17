# 🎓 EduNext – A Smart Educational Platform

EduNext is a modern and intelligent educational platform designed to enhance digital learning, coding practice, forum discussions, event participation, certification, and much more — all in a unified ecosystem. It is built with a **microservices architecture** using **Spring Boot**, **Angular**, **MongoDB**, **MySQL**, and **Docker**, and integrates **Eureka** and **API Gateway** for service discovery and routing.

---

## 🌟 Project Overview

EduNext is an all-in-one platform for:

- 👨‍🎓 **Students** to:
  - Solve programming problems.
  - Participate in coding games & submit GitHub links.
  - Earn scores and rankings.
  - Discuss topics in forums and threads.
  - Reserve and attend technical events and hackathons.

- 🧑‍🏫 **Administrators** to:
  - Manage problems, events, and certifications.
  - Review student submissions.
  - Generate statistics and dashboards.
  - Generate and manage certificates (via Python Flask + MongoDB).

---

## 🚀 Technologies Used

### 💻 Backend (Microservices)
- `Spring Boot` for Java microservices
- `Flask` for Certificate Service (Python)
- `MySQL` for relational data (user, coding game, forum, etc.)
- `MongoDB` for NoSQL data (certificates)
- `Eureka` for service discovery
- `Spring Cloud Gateway` as an API Gateway
- `Docker` for containerization
- `Docker Compose` for orchestration

### 🖥 Frontend
- `Angular 16` for responsive UI
- `ng2-charts` for dashboards
- `SCSS/CSS` for styling
- `JWT`-based authentication
- `Dynamic routing` and `modular architecture`

---

## 👩‍💻 My Contributions

As the lead developer of this project, I focused on both frontend and backend functionalities with an emphasis on **DevOps**, **microservice communication**, and **feature-rich UX/UI**. Here's what I implemented:

### 🧠 Backend – Microservices (Spring Boot)
- Built the **Coding Game microservice** with entities: `Problem`, `Submission`, `Language`, `Compiler`.
- Implemented full CRUD operations, pagination, scoring logic, and GitHub link submission.
- Developed the **Forum microservice**: `Forum`, `Thread`, `Blog`, `Reaction`, with advanced interaction logic.
- Created the **Event microservice**: reservation system, ticket management, and mailing system.
- Developed advanced **JPQL statistics endpoints** for dashboards.
- Integrated with **API Gateway** and **Eureka** for full microservice registration and routing.

### 💬 Frontend – Angular Modules
- `Coding Game` interface with:
  - Code editor (connected to Judge0)
  - Problem list, detail view, and real-time submission
  - GitHub link submission & auto-scoring
- `Forum & Blog` management with like/comment reactions
- `Events & Reservations` interface with:
  - Event cards, booking logic, chatbot assistant
- `Admin Dashboard` with:
  - Submission stats, leaderboards, and analytics
  - PDF download for certificates
- Dynamic `Sidebar` navigation and route integration for modules

### 🔧 DevOps & Containerization
- Wrote multiple `Dockerfiles` for each service
- Set up `docker-compose.yml` to orchestrate:
  - 7 Spring Boot microservices
  - Eureka & API Gateway
  - MongoDB & MySQL
  - Flask (Python) Certificate Service
- Ensured all services run and communicate correctly in containers

---

## 📈 Features Summary

| Feature | Description |
|--------|-------------|
| 👨‍💻 Code Submission | Students submit solutions with GitHub links and receive scores |
| 📊 Admin Dashboards | View charts: submissions per problem, best student by score |
| 🧵 Forum System | Blog and thread discussion with reactions (Like, Love, Comment, etc.) |
| 🗓️ Event Module | List of events, reservations, and ticketing |
| 📄 Certificate Generation | Certificates auto-generated with Flask and downloadable |
| 🧠 Smart Routing | API Gateway + Eureka for scalable routing |
| 🤖 Chatbot | Smart assistant embedded in event module for guidance |
| 🛠️ Fully Dockerized | Microservices run independently in containers |

---
✨ Motivation
EduNext was born from a passion for building meaningful digital learning experiences. As a software engineer driven by innovation, 
I wanted to create a scalable, interactive, and intelligent platform that empowers students and simplifies admin tasks.
This project reflects my love for backend architecture, clean UI design, and full-stack development – all working together to enhance education through technology.
