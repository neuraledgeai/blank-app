import streamlit as st
from database import LocalDatabase

db = LocalDatabase()
data = db.loadData()

st.title(f"hi")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
