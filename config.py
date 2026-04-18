import os
from dotenv import load_dotenv
import json

load_dotenv()
 
AI_API_KEY = os.getenv("AI_API_KEY")
 
APP_TITLE = "FinAIzer - AI Financial Advisor"
import firebase_admin
from firebase_admin import credentials, firestore, auth

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:

    if os.path.exists("firebase_config.json"):
        cred = credentials.Certificate("firebase_config.json")
    else:
        cred_dict = json.loads(os.environ["FIREBASE_KEY"])
        cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(cred)

db = firestore.client()