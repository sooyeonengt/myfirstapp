import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="귀여운 포켓몬 갤러리", page_icon="🐾", layout="centered")

st.title("🐾 귀여운 포켓몬 갤러리")
st.write("아래는 실제 존재하는 귀여운 포켓몬 이미지들입니다!")

# 포켓몬 이미지 정보 (이름과 이미지 URL)
pokemon_images = [
    {"name": "피카츄", "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png"},
    {"name": "이브이", "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png"},
    {"name": "푸린", "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png"},
    {"name": "팽도리", "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/393.png"},
    {"name": "치코리타", "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/152.png"}
]

# 포켓몬 이미지 보여주기
for p in pokemon_images:
    st.subheader(p["name"])
    st.image(p["url"], use_column_width=True)

st.success("모두 다 귀엽죠? 😊")
