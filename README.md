# 📄 AI Resume Skill Gap Analyzer

An AI-powered Resume Screening System that compares a candidate's resume with a Job Description (JD), calculates an ATS (Applicant Tracking System) match score, identifies missing skills, and recommends learning resources to improve employability.

---

## 📌 Project Overview

Recruiters receive hundreds of resumes for a single job opening. Manually checking every resume is time-consuming and inefficient.

This project automates the resume screening process by using Artificial Intelligence techniques to:

- Extract skills from resumes
- Extract required skills from Job Descriptions
- Compare both skill sets
- Calculate ATS Match Score
- Identify missing skills
- Recommend learning resources for improvement

---

# 🚀 Features

✅ PDF Resume Upload

✅ Resume Text Extraction

✅ Resume Preprocessing

✅ Technical Skill Extraction

✅ Job Description Analysis

✅ Skill Matching

✅ Missing Skill Detection

✅ Extra Skill Detection

✅ ATS Score Calculation

✅ Skill Gap Recommendations

✅ Learning Resource Suggestions

---

# 🛠 Technologies Used

## Programming Language

- Python 3.13

## Frontend

- Streamlit

## Libraries

- Pandas
- PyPDF2
- Regular Expressions (Regex)
- NLTK

## Dataset

- Technical Skills Database (CSV)
- Skill Recommendation Database (CSV)

---

# 📂 Project Structure

```
AI Resume Skill Gap Analyzer/
│
├── assets/
│   ├── logo.png
│   └── style.css
│
├── data/
│   ├── processed/
│   │   └── technical_skills_database.csv
│   │
│   └── raw/
│       ├── skill_recommendations.csv
│       ├── programming_languages.csv
│       ├── machine_learning.csv
│       ├── deep_learning.csv
│       ├── cloud.csv
│       └── ...
│
├── uploads/
│
├── outputs/
│
├── models/
│
├── scripts/
│
├── utils/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── recommender.py
│   └── jd_parser.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Skill-Gap-Analyzer.git
```

## Open the Project

```bash
cd AI-Resume-Skill-Gap-Analyzer
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

# 📊 Workflow

1. Upload Resume (PDF)

↓

2. Extract Resume Text

↓

3. Clean Resume Text

↓

4. Extract Resume Skills

↓

5. Paste Job Description

↓

6. Extract JD Skills

↓

7. Compare Skills

↓

8. Calculate ATS Score

↓

9. Identify Missing Skills

↓

10. Recommend Skills & Learning Resources

---

# 🧠 ATS Score Calculation

ATS Score is calculated based on the percentage of Job Description skills found in the candidate's resume.

Formula:

```
ATS Score =
(Matched Skills / Total JD Skills) × 100
```

---

# 📈 Example Output

Resume Skills

- Python
- TensorFlow
- SQL
- Flask
- GitHub

Missing Skills

- Docker
- AWS

ATS Score

```
75%
```

Recommendation

- Learn Docker
- Learn AWS
- Follow recommended learning resources

---

# 🎯 Future Improvements

- NLP-based semantic skill matching
- AI Resume Ranking
- Resume Quality Feedback
- Experience Matching
- Education Matching
- Resume Keyword Optimization
- Multiple Resume Comparison
- Recruiter Dashboard
- AI Interview Question Generator

---

# 👨‍💻 Author

**M DINESH**

B.Tech – Artificial Intelligence & Data Science

Project – AI Resume Skill Gap Analyzer

---

# 📄 License

This project is developed for educational purposes as part of the B.Tech Project.