# 🎓 AI & ML Student Management System

A terminal-based **Student Management System** built using **Python** and **MySQL**, integrated with **Artificial Intelligence**, **Machine Learning**, and **Data Analytics**. The system helps manage student records, predict placement readiness, forecast academic performance, and provide AI-powered assistance.

---

## 🚀 Features

### 📚 Student Management
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
- Secure Admin Authentication

### 🤖 AI Features
- AI Resume Summary
- AI Chatbot (Google Gemini API)

### 🧠 Machine Learning
- Placement Prediction (Random Forest Classifier)
- Performance Prediction (Linear Regression)

### 📊 Analytics
- Placement Distribution (Pie Chart)

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Database | MySQL |
| AI | Google Gemini API |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Model Storage | Joblib |
| Visualization | Matplotlib |

---

## 📂 Project Structure

```text
AI-ML-Student-Management-System/
│
├── .env
├── .env.example
├── .gitignore
│
├── student.py
├── database.py
├── ui.py
├── admin.py
├── student_operations.py
├── ai_features.py
├── ml_features.py
├── analytics.py
│
├── placement_dataset.csv
├── performance_dataset.csv
│
├── train_placement_model.py
├── train_performance_model.py
│
├── placement_model.pkl
├── performance_model.pkl
│
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Models

### Placement Prediction

**Algorithm**
- Random Forest Classifier

**Input Features**
- Marks
- Attendance
- Projects
- Communication Skills
- Internships
- CGPA

**Output**
- Placement Status
- Placement Confidence
- Placement Readiness
- Estimated Salary
- Company Eligibility
- Personalized Recommendations

---

### Performance Prediction

**Algorithm**
- Linear Regression

**Input Features**
- Marks
- Attendance
- Projects
- Internships
- CGPA

**Output**
- Predicted Next Semester Marks
- Performance Level
- Improvement Suggestions

---

## 📊 Analytics Dashboard

The system provides visualization using **Matplotlib**.

Current Analytics:

- 🥧 Placement Distribution (Pie Chart)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-ML-Student-Management-System.git
cd AI-ML-Student-Management-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=students_db

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Create the MySQL Database

Create a database named:

```sql
students_db
```

Import your database schema or create the required tables before running the application.

### 5. Train Machine Learning Models

```bash
python train_placement_model.py
python train_performance_model.py
```

This generates:

- placement_model.pkl
- performance_model.pkl

### 6. Run the Application

```bash
python student.py
```

---

## 💻 Main Menu

```text
=========== STUDENT MANAGEMENT ===========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student

=============== AI FEATURES ==============

6. AI Resume Summary
7. AI Chatbot

============= ML FEATURES ================

8. ML Placement Prediction
9. ML Performance Prediction
10. ML Student Analytics

11. Exit
```

---

## 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Python Programming
- MySQL Database Integration
- CRUD Operations
- Artificial Intelligence Integration
- Machine Learning Model Development
- Data Visualization with Matplotlib
- Modular Software Architecture
- Secure Environment Variable Management
- Clean Code Organization

---

## 🔮 Future Improvements

- Email Notifications
- PDF Resume Generation
- Student Login System
- Faculty Dashboard
- Web-Based Version using Flask or Django
- Additional Analytics Visualizations
- Enhanced Machine Learning Models

---

## 👨‍💻 Author

**Vijay Rama Reddy Karri**

📧 Email: **kvijayramareddy@gmail.com**

🔗 LinkedIn:  
https://www.linkedin.com/in/vijayramareddykarri

💻 GitHub:  
https://github.com/v-i-j-ay

🌐 Portfolio:  
https://kvrportfolio.vercel.app/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
