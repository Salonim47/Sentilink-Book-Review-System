# Sentilink Enterprise — Book Review Sentiment & Analytics Platform

An enterprise-grade, 3-Tier Web Application and Analytics Dashboard designed for **Book Review Sentiment Analysis**, integrating the university curricula of **Enterprise Systems**, **Advanced Text Analytics**, and **IT Project Management (ITPM)**.

---

## 🚀 Key Features

1. **Strict Role-Based Access Control (RBAC)**:
   - **Customer Portal**: Browse Kaggle/Goodreads book catalog, view ratings and sentiment breakdowns, explore reader emotion radars, and submit reviews with live feedback.
   - **Admin Command Center (Segregated)**: Executive CRM dashboard, Customer Churn Risk radar, Model Benchmark Lab, Security Audit Trail with SHA-256 signatures, Book Catalog management, and Agile Scrum / PERT-CPM project scheduler.
   - **Quick 1-Click Dummy Credentials**:
     - **Admin**: `admin` / `admin123`
     - **Customer**: `customer` / `customer123`

2. **Advanced NLP & Text Mining Engine**:
   - **Preprocessing Pipeline (Unit I)**: Tokenization, Stopword removal, Morphological reduction (Stemming/Lemmatization).
   - **Sentiment Analysis (Unit II)**: Polarity $(-1.0 \text{ to } +1.0)$, Subjectivity $(0.0 \text{ to } 1.0)$, Confidence estimation, and 5-class Emotion breakdown (Joy, Surprise, Sadness, Anger, Fear).
   - **Aspect-Based Sentiment**: Dissects specific narrative aspects (*Plot*, *Characters*, *Writing Style*, *Pacing*, *Emotional Depth*).
   - **RAKE Keyphrase Extraction (Unit III)**: Automated candidate keyphrase discovery based on word degree and co-occurrence frequency matrices.
   - **ML Benchmark Lab (Unit III)**: Supervised Scikit-Learn TF-IDF + Multinomial Naive Bayes evaluation generating Precision, Recall, F1-Score, and a dynamic Confusion Matrix.

3. **Enterprise CRM & Security Governance**:
   - **CRM Customer Intelligence**: Customer Satisfaction Index (CSAT), Temporal Sentiment Trend (2024–2026), and high-risk customer churn flags.
   - **Cryptographic Audit Trail (Unit III)**: Immutable event logging for logins, reviews, and admin moderations using SHA-256 digital digests.

4. **IT Project Management (ITPM)**:
   - **Agile Scrum Kanban Board (Unit V)**: Sprint backlogs, story points, task transitions.
   - **PERT / CPM Scheduler (Unit II & III)**: Three-point estimation, Expected duration $t_e = (a + 4m + b)/6$, Activity variance, Critical Path determination, and 95% confidence intervals.

---

## 🛠️ Technology Stack

- **Presentation Tier**: HTML5, Modern Glassmorphism, Tailwind CSS, Chart.js, Lucide Icons, Vanilla JavaScript (AJAX/Fetch).
- **Application / Controller Tier**: Python 3.13, FastAPI (Asynchronous ASGI framework), Uvicorn.
- **Data / DBMS Tier**: SQLite 3 Relational Database (`enterprise_books.db`), Normalized schema with foreign keys and CASCADE constraints.
- **Machine Learning & Text Mining**: Scikit-Learn, NumPy, Custom RAKE Keyword Extractor, Domain Lexicons.

---

## 🏃 Quick Start Guide

### 1. Prerequisites
Ensure Python 3.10+ (or the `py` launcher) is installed.

### 2. Start the Enterprise Server
Open a terminal in the project directory and run:

```bash
cd "c:\Users\mail2\OneDrive\Documents\BookReview-Sentiment-Enterprise-System"
py server.py
```

### 3. Open the Web Application
Open your browser and navigate to:
**`http://127.0.0.1:8000`**

### 4. Exploring the Dashboards
- **As Customer**: Click `Customer: customer/customer123` to test standard reader features, browse books, open the Book Modal to view aspect breakdowns, or visit the **Live NLP Reviewer** to type reviews and observe real-time tokenization and sentiment meters.
- **As Admin**: Click `Admin: admin/admin123` to unlock the **Admin Command Center**. Inspect CRM metrics, test the ML Benchmark evaluation to view the Confusion Matrix, review the SHA-256 Security Audit Trail, or navigate the Agile Scrum Kanban Board and PERT/CPM Critical Path analysis.
