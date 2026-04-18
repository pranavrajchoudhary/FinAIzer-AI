import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, firestore

# ---------------- AI KEY ---------------- #
try:
    AI_API_KEY = st.secrets["AI_API_KEY"]
except Exception as e:
    st.error("AI_API_KEY not found in secrets")
    st.stop()

# ---------------- FIREBASE ---------------- #
try:
    if not firebase_admin._apps:
        raw_cred = st.secrets["FIREBASE_CREDENTIAL"]

        # Debug (SAFE)
        st.write("DEBUG: Credential length =", len(raw_cred))

        cred_dict = json.loads(raw_cred)

        # Debug (SAFE)
        st.write("DEBUG: Firebase project =", cred_dict.get("project_id"))

        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)

    db = firestore.client()

except KeyError:
    st.error("FIREBASE_CREDENTIAL missing in secrets")
    st.stop()

except json.JSONDecodeError as e:
    st.error("JSON parsing failed. Your FIREBASE_CREDENTIAL is invalid.")
    st.text(str(e))
    st.stop()

except Exception as e:
    st.error("Firebase initialization failed")
    st.text(str(e))
    st.stop()
