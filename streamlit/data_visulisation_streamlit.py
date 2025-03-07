import streamlit as st

import pandas as pd

import numpy as np

st.title("bar_chart")

df=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(df)



st.title("bar_chart")
st.line_chart(df)