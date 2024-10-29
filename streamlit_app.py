import streamlit as st
from database import LocalDatabase
from business import Model

#db = LocalDatabase()
#df = db.getDataFrame()

ds = Model()
model = ds.makeForecast()
st.title(f"From Data Serverjjjjj: {model}, okay")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
#st.dataframe(df)
