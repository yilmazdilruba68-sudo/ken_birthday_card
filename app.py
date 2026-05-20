import streamlit as st
import time

# Sayfa ayarlarımızı yapalım
st.set_page_config(page_title="You have a letter! 💌", page_icon="💙", layout="centered")

# Sayfa başlığı ve tatlı bir arka plan efekti için CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E1F5FE; /* Alice Blue - Çok Açık Mavi */
    }
    .ana-baslik {
        text-align: center; 
        color: #01579B; /* Navy Blue - Koyu Mavi Başlık */
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem;
        font-weight: bold;
        padding: 20px;
    }
    .mesaj-kutusu {
        border: 2px solid #81D4FA; /* Açık Mavi Çerçeve */
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlığımızı ekrana basalım
st.markdown("<div class='ana-baslik'>This for you!(o・ω・o) ✨</div>", unsafe_allow_html=True)

st.write("\n" * 2)

# Kullanıcıyı etkileşime sokacak harika bir buton tasarlayalım
st.write("### 💌 ボタンを押してください!")

if st.button("✉️ 手紙を開けて", use_container_width=True):
    # Sayfaya rengarenk konfetiler fırlatalım (Bunun açılmama şansı yok!)
    st.balloons()

    time.sleep(0.5)

    # Ekrana tatlı bir kutu içinde doğum günü mesajımızı getirelim
    st.markdown(
        """
        <div class='mesaj-kutusu'>
            <h2 style='color: #ff6b6b;'>🎉 HAPPY BİRTHDAY! 🎉</h2>
            <p style='color: #4a4a4a; font-size: 1.2rem;'>
                お誕生日おめでとう！ また一つ歳を取ったね , <br>
                たくさん幸せがありますように！♪ヽ(´▽｀)/ 💫
            </p>
            <p style='font-size: 2rem;'>⚽🪿✈️🌍🐳</p>
        </div>
        """,
        unsafe_allow_html=True
    )

