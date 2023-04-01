import streamlit as st
from datetime import time, datetime

st.header("Slider Kullanımı..")

st.subheader("Slider")

age = st.slider("Kaç Yaşındasın ?", 0, 100, 11)
st.write("Ben ", age, " yaşındayım.")

st.subheader("Range Slider")


