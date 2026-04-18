from groq import Groq
from config import AI_API_KEY
import hashlib
import streamlit as st

client = Groq(api_key=AI_API_KEY)


# ---------------- SYSTEM PROMPT ---------------- #
BASE_SYSTEM_PROMPT = """
Act as a fintech financial advisor.
Be concise, practical, and numeric.
Avoid generic advice.
"""


# ---------------- HELPERS ---------------- #
def _cache_key(data):
    return hashlib.md5(str(data).encode()).hexdigest()


def _detect_language(text):
    try:
        text.encode('ascii')
        return "en"
    except:
        return "non-en"


def _currency_by_lang(lang):
    return "₹" if lang == "en" else "$"


# ---------------- INTERNAL CORE ---------------- #
def generate_financial_advice(data):

    prompt = f"""
You are a professional financial advisor.

User Financial Data
Income: {data['income']}
Expenses: {data['expenses']}
Savings: {data['savings']}
Debt: {data['debt']}
Savings Ratio: {data['savings_ratio']}%
Debt Ratio: {data['debt_ratio']}%
Goal: {data['goal']}

Return advice EXACTLY in this format:

BUDGET:
- suggestion
- suggestion

SAVINGS:
- suggestion
- suggestion

DEBT PLAN:
- suggestion
- suggestion

INVESTMENT:
- suggestion
- suggestion

GOAL STRATEGY:
- suggestion
- suggestion
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": BASE_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content

@st.cache_data(show_spinner=False)
def finance_chatbot_response(question, profile=None):

    context = ""

    if profile:
        context = f"""
User Context:
Name: {profile.get('name')}
Risk: {profile.get('risk')}
Goal: {profile.get('goal')}
"""

    prompt = f"""
{context}

User Question:
{question}

Instructions:
- Answer in a helpful, financial advisor tone
- Keep it concise
- If relevant, relate answer to user's goal or risk profile
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": BASE_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content    