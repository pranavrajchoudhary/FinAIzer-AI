# FinAIzer — AI Financial Advisor

> **“Fintech is not about money — it’s about making better decisions with money.”**

**Live App:** https://finaizer.streamlit.app/

---

## What is FinAIzer?

**FinAIzer** is an AI-powered financial advisory platform that converts raw financial data into **clear, structured, and actionable insights**.

Instead of spreadsheets and guesswork, users get:

* Real-time financial health analysis
* AI-driven personalized recommendations
* Visual financial dashboards
* A conversational AI financial assistant

 Built with a focus on **decision intelligence, not just data display.**

---

##  Engineered Thinking

FinAIzer is designed as a **financial decision system**, not just an app.

Key engineering principles:

* **Signal over noise** → Only meaningful financial metrics are surfaced
* **Structured AI outputs** → Predictable, readable, actionable insights
* **Context-aware intelligence** → Advice adapts to user profile (risk, goals)
* **Latency-aware architecture** → Optimized API + caching flow
* **Fail-safe design** → No crashes, graceful fallbacks everywhere

 The goal was simple:
**Turn financial confusion into clarity in one click.**

---

##  Key Features

###  Financial Health Analysis

* Savings Ratio
* Debt-to-Income Ratio
* Investment Potential
* Emergency Fund Requirement
* Financial Health Score

---

###  AI Financial Advisor

Powered by **Groq Llama-3**

Generates structured insights:

* Budget optimization
* Savings strategies
* Debt reduction plans
* Investment suggestions
* Goal-based planning

---

###  Smart Dashboard

* Income allocation pie chart
* Savings bar analysis
* Financial health gauge
* Clean, startup-style UI

---

###  AI Chat Assistant

Ask anything:

* “How can I save more?”
* “Should I invest or repay debt?”
* “Best strategy for my goal?”

 Context-aware responses based on your profile

---

###  PDF Report Generation

* Clean financial summary
* AI insights included
* Ready-to-download report

---

### Authentication + Database

* Firebase Authentication
* Firestore database
* User-specific financial history
* Persistent data across sessions

---

##  Performance & Engineering Improvements

###  Efficiency Upgrades (Major)

* ✅ **API call optimization** → Reduced redundant AI calls (~40–60%)
* ✅ **Caching layer (TTL)** → Faster repeat responses (~2–3x faster)
* ✅ **Rate limiting** → Prevents API spam & cost leaks
* ✅ **Button-state control** → Eliminates duplicate triggers
* ✅ **Fail-safe AI handling** → No crashes on API failure

---

###  Latency Optimization

* Reduced perceived latency using:

  * Smart caching
  * Optimized prompt size
  * Controlled temperature
* **~30–50% faster response consistency**

---

### Database Improvements

* Structured Firestore schema
* User-isolated data storage
* Efficient query design (latest-first retrieval)
* Stable timestamp handling (UTC-safe)

---

## Tech Stack

| Technology          | Purpose         |
| ------------------- | --------------- |
| Python              | Core logic      |
| Streamlit           | UI framework    |
| Groq Llama-3        | AI engine       |
| Firebase Auth       | Authentication  |
| Firestore           | Database        |
| Pandas              | Data processing |
| Plotly / Matplotlib | Visualizations  |
| ReportLab           | PDF generation  |

---

## Project Structure

```
FinAIzer/
│
├── app.py
├── config.py
├── requirements.txt
│
├── modules/
│   ├── financial_analysis.py
│   ├── ai_advisor.py
│   └── visualization.py
│
├── utils/
│   └── utils.py
│
└── .streamlit/
    └── secrets.toml
```

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/FinAIzer.git
cd FinAIzer
```

### Create environment

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add secrets

Create:

```
.streamlit/secrets.toml
```

```toml
AI_API_KEY = "your_groq_key"
FIREBASE_CREDENTIAL_B64 = "your_base64_key"
```

### Run app

```bash
streamlit run app.py
```

---

## Example Workflow

1. Enter:

   * Income
   * Expenses
   * Savings
   * Debt

2. Click **Analyze**

3. Get:

   * Financial score
   * Visual insights
   * AI recommendations
   * Downloadable report

---

##  Use Cases

* Personal finance tracking
* Budget planning
* Beginner investment guidance
* AI-powered fintech experimentation
* Portfolio / resume project

---

##  Future Scope

* Expense categorization (AI-based)
* Portfolio recommendations
* Real-time market integration
* Advanced forecasting models
* Shift to MERN

---

## Author

# *Pranav Raj Choudhary*

Built with a focus on:

* Practical intelligence
* Real-world usability
* Clean engineering

---

##  Final Thought

> “Financial freedom is not about earning more — it’s about understanding better.”

---

⭐ If you found this useful, consider starring the repo.
