import streamlit as st

def main():
    st.title("Kişisel Web Sitem")

    menu = ["Anasayfa", "Hakkımda", "Proje Portföyü", "İletişim"]
    choise = st.sidebar.selectbox("Menü",menu)

    if choise == "Anasayfa":
        st.subheader("Hoşgeldiniz.")
        st.write("Bu benim kişisel web sitem.")

    elif choise == "Hakkımda":
        st.subheader("Hakkımda")
        st.write("Ben bir veri bilimciyim. Streamlit ile interaktif uygulamalar oluşturmayı seviyorum.")

    elif choise == "Proje Portföyü":
        st.subheader("Proje Portföyü")
        st.write("Aşağıda bazı projelerim yer almaktadır.")

        st.write("- Proje 1")
        st.write("- Proje 2")
        st.write("- Proje 3")

    elif choise == "İletişim":
        st.subheader("İletişim")
        st.write("Benimle aşağıdaki sosyal medya araçları ile iletişime geçebilirsiniz.")

        st.write("- E-posta : example@gmail.com")
        st.write("- Linkedin : https://linkedin.com/ahmet_karakaya2333")
        st.write("- Github : https://github.com/karakayaahmet")

    
if __name__ == "__main__":
    main()