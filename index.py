import streamlit as st
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('private/raspberry1-47370-firebase-adminsdk-9eb4u-92da494d53.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("光線和距離即時監測")




def downloadData():
    print("下載資料")

