import streamlit as st
from database import LocalDatabase
from business import DataServer

#db = LocalDatabase()
#df = db.getDataFrame()

ds = DataServer()
model = ds.makeForecast()
st.title(f"From Data Serverjjjjj: {model}")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
#st.dataframe(df)
