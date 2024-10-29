import streamlit as st
from database import LocalDatabase
from business import Model

#db = LocalDatabase()
#df = db.getDataFrame()

model = Model()
forcasted_df = model.makeForecast(years = range(1,3))
st.title(f"From Data Server okay")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.dataframe(forcasted_df)
