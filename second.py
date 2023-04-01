import streamlit as st

st.header("Buton Kullanımı")

if st.button("Selam Söyle"):
    st.write("Selamlar")

else:
    st.write("Tekrardan görüşmek dileğiyle...")
