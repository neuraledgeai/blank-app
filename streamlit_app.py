import streamlit as st
from database import LocalDatabase

db = LocalDatabase()
data = db.loadData()

st.title("🎈 My new app Hii")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
