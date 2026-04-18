import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, firestore

# ---------------- AI KEY ---------------- #
AI_API_KEY = st.secrets["AI_API_KEY"]

# ---------------- FIREBASE ---------------- #
if not firebase_admin._apps:
    cred_dict = json.loads(st.secrets["FIREBASE_CREDENTIAL"])
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()