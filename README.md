# 🚀 AI Career Copilot

**AI Career Copilot** is an AI-powered placement preparation platform that helps students prepare for technical interviews through resume analysis, AI mock interviews, coding practice, and personalized career roadmaps.

The platform integrates **FastAPI, Streamlit, MongoDB, and AI APIs** to provide an intelligent career assistant for students.

---

# 📌 Features

### 🔐 Authentication System

* Secure **Login & Registration**
* **Role-Based Access Control**
* Separate dashboards for **Students and Admin**

---

### 📄 Resume Analyzer

* Upload resume (PDF)
* AI extracts key skills and experience
* Provides **resume improvement suggestions**

---

### 📑 Job Description (JD) Analyzer

* Analyze job descriptions
* Extract:

  * Required skills
  * Responsibilities
  * Experience level
* Generate preparation insights based on JD

---

### 🎤 AI Mock Interview

* AI generates interview questions
* Students answer through text or voice
* AI evaluates responses and provides:

  * Score
  * Feedback
  * Improvement suggestions

---

### 📊 Interview History & Progress Tracking

* Stores interview attempts in database
* Students can view:

  * Previous interview scores
  * Question history
* Visual progress chart showing improvement over time

---

### 💻 Coding Practice

* Practice technical interview questions
* Focus on **Data Structures & Algorithms**

---

### 🧭 Career Roadmap Generator

* Generates personalized learning roadmap
* Based on:

  * Target role
  * Required skills
  * AI analysis

---

### 🤖 AI Career Chat

* AI assistant for career guidance
* Helps with:

  * Interview preparation
  * Skill learning
  * Resume advice
  * Career planning

---

### 🎙 Voice Interview Mode

* Speech-to-text interview system
* Uses **Vosk speech recognition**
* Simulates real interview environment

---

### 👨‍💼 Admin Dashboard

Admins can:

* Monitor users
* View interview analytics
* Track platform activity

---

# 🏗 System Architecture

```
Frontend (Streamlit)
        ↓
FastAPI Backend (API Layer)
        ↓
AI Services (LLM / NLP / Speech)
        ↓
MongoDB Database
```

---

# 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Python

### Database

* MongoDB Atlas

### AI / NLP

* Grok AI
* spaCy

### Speech Recognition

* Vosk

### DevOps

* Docker
* GitHub Actions

---

# 📂 Project Structure

```
ai-career-copilot
│
├── backend
│   ├── main.py
│   ├── routes
│   ├── models
│   ├── database
│   └── ai_services
│
├── frontend
│   ├── app.py
│   ├── views
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── dashboard.py
│   │   ├── mock_interview.py
│   │   ├── resume_analyzer.py
│   │   ├── jd_analyzer.py
│   │   ├── career_roadmap.py
│   │   └── interview_history.py
│
├── models
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-career-copilot.git
cd ai-career-copilot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 5️⃣ Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

# 📊 Example Workflow

```
Register / Login
      ↓
Upload Resume
      ↓
Analyze Job Description
      ↓
Take AI Mock Interview
      ↓
View Score & Feedback
      ↓
Track Interview Progress
      ↓
Follow Career Roadmap
```

---

# 🎯 Use Cases

* Placement preparation platform for students
* AI-powered career assistant
* Interview training system
* Resume analysis tool

---

# 🔮 Future Improvements
*Performance & improvement
* ATS resume scoring
* Job recommendation system

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed by **Rupavathy**
Computer Science Undergraduate
