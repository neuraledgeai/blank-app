import streamlit as st
from database import LocalDatabase

db = LocalDatabase()
df = db.getDataFrame()

st.title(f"From database")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.DataFrame(df)
