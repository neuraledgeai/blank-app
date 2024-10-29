import streamlit as st
from database import LocalDatabase
from business import Model
from display import IndiaGDPApp

#db = LocalDatabase()
#df = db.getDataFrame()

#model = Model()
# When it is 1, it means 0. 
#forcasted_df = model.makeForecast(years = range(1, 11))

app = IndiaGDPApp()
st.title(f"From Data Server okay sjjsss")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
#st.dataframe(forcasted_df)
fig = app.forecast(years = 11)
st.dataframe(fig)
#st.plotly_chart(fig)
