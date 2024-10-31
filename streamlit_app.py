import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

#pc = PresentationComponents()
db = LocalDatabase()
#df = db.getDataFrame()

df = db.loadData()
#model = Model()
# When it is 1, it means 0. 
#forcasted_df = model.makeForecast(years = range(1, 11))

#app = IndiaGDPApp()
st.title(f"From Data Server {df["Year"].dtype} okay sjjsss")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.dataframe(df)
#app.forecast(years = 11)
#st.subheader("GDP Forecast :blue[Bar Chart]")
#years = st.slider("Forecast Horizon", 0, 20, 5)
#pc.forecast_line_chart(years = years+1)
