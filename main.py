import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI LoL 챔피언 추천기", page_icon="🎮", layout="centered")

st.title("🎮 MBTI별 LoL 챔피언 추천기")
st.caption("당신의 성격 유형에 어울리는 챔피언 3명을 추천해드려요!")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI - 챔피언 추천 딕셔너리
mbti_champions = {
    "INTJ": ["Swain", "Mordekaiser", "Vel'Koz"],
    "INTP": ["Heimerdinger", "Zilean", "Singed"],
    "ENTJ": ["Jarvan IV", "Camille", "Jayce"],
    "ENTP": ["Ekko", "Jhin", "Qiyana"],
    "INFJ": ["Karma", "Ivern", "Soraka"],
    "INFP": ["Yuumi", "Lillia", "Neeko"],
    "ENFJ": ["Galio", "Taric", "Orianna"],
    "ENFP": ["Lux", "Nami", "Rakan"],
    "ISTJ": ["Shen", "Trundle", "Sejuani"],
    "ISFJ": ["Braum", "Amumu", "Sona"],
    "ESTJ": ["Leona", "Vi", "Poppy"],
    "ESFJ": ["Lulu", "Morgana", "Janna"],
    "ISTP": ["Zed", "Kayn", "Graves"],
    "ISFP": ["Ahri", "Xayah", "Seraphine"],
    "ESTP": ["Lee Sin", "Draven", "Samira"],
    "ESFP": ["Ezreal", "Miss Fortune", "Fizz"]
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

# 추천 버튼
if st.button("챔피언 추천받기! 💡"):
    champions = mbti_champions.get(selected_mbti, [])
    st.subheader(f"✨ {selected_mbti} 유형에게 어울리는 챔피언:")
    for champ in champions:
        st.markdown(f"- **{champ}**")
    st.success("행운을 빕니다! 승리를 향해~ 🎉")
