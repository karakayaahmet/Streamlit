import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Yazı Tip Çalışmaları..")

st.write('Merhabalar *Herkese!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    "birinci sütun" : [1,2,3,4,5],
    "ikinci sütun" : [6,7,8,9,10]
})

st.write(df)

st.write("Below is a dataframe:", df, "Above is a dataframe")
