import streamlit as st

# MBTI 추천 데이터
mbti_data = {
    "INTJ": {
        "desc": "전략적인 사고와 장기적 계획에 능숙한 마스터마인드 유형입니다.",
        "champions": [
            {"name": "Swain", "desc": "지휘관 같은 존재로, 전장의 흐름을 통제합니다.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Swain_0.jpg"},
            {"name": "Mordekaiser", "desc": "혼자서도 적을 지배하는 강력한 존재감.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Mordekaiser_0.jpg"},
            {"name": "Vel'Koz", "desc": "논리와 지식에 집착하는 비전 생물체.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Velkoz_0.jpg"}
        ]
    },
       "INTP": {
        "desc": "호기심 많고 분석적인 철학자 유형입니다.",
        "champions": [
            {"name": "Heimerdinger", "desc": "천재 과학자로 발명에 집착합니다.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Heimerdinger_0.jpg"},
            {"name": "Zilean", "desc": "시간을 조작하며 지식을 추구하는 마법사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zilean_0.jpg"},
            {"name": "Singed", "desc": "광기의 과학자, 비정통적 사고의 대명사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Singed_0.jpg"}
        ]
    },
    "ENTJ": {
        "desc": "리더십과 조직 능력이 뛰어난 지휘관 유형입니다.",
        "champions": [
            {"name": "Jarvan IV", "desc": "민족을 위해 싸우는 왕자이자 전쟁의 지휘관.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/JarvanIV_0.jpg"},
            {"name": "Camille", "desc": "정밀한 판단력과 날카로운 움직임의 첩보원.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Camille_0.jpg"},
            {"name": "Jayce", "desc": "기술과 이상을 추구하는 진보적 영웅.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jayce_0.jpg"}
        ]
    },
    "ENTP": {
        "desc": "아이디어가 풍부하고 창의적인 발명가형입니다.",
        "champions": [
            {"name": "Ekko", "desc": "시간을 조작하는 천재 소년.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ekko_0.jpg"},
            {"name": "Jhin", "desc": "예술과 죽음을 결합한 표현주의적 암살자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_0.jpg"},
            {"name": "Qiyana", "desc": "자연의 원소를 다루는 당당한 여왕.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Qiyana_0.jpg"}
        ]
    },
    "INFJ": {
        "desc": "이상주의적이고 타인을 돕고자 하는 조언자 유형입니다.",
        "champions": [
            {"name": "Karma", "desc": "평화를 지키려는 강한 의지의 정신 지도자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Karma_0.jpg"},
            {"name": "Ivern", "desc": "자연을 아끼는 다정한 수호자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ivern_0.jpg"},
            {"name": "Soraka", "desc": "희생과 치유의 상징인 별의 아이.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Soraka_0.jpg"}
        ]
    },
    "INFP": {
        "desc": "따뜻하고 이상주의적인 성격의 중재자입니다.",
        "champions": [
            {"name": "Yuumi", "desc": "귀여운 마법 고양이로 친구를 보호합니다.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yuumi_0.jpg"},
            {"name": "Lillia", "desc": "수줍은 사슴 소녀로 꿈의 세계를 지킵니다.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lillia_0.jpg"},
            {"name": "Neeko", "desc": "호기심 많고 다정한 변신 능력자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Neeko_0.jpg"}
        ]
    },
    "ENFJ": {
        "desc": "사람을 이끄는 데에 뛰어난 카리스마 있는 리더형입니다.",
        "champions": [
            {"name": "Galio", "desc": "동료를 보호하기 위한 정의로운 거상.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Galio_0.jpg"},
            {"name": "Taric", "desc": "아름다움과 보호의 기사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Taric_0.jpg"},
            {"name": "Orianna", "desc": "조화롭고 우아한 감성의 인공 생명체.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Orianna_0.jpg"}
        ]
    },
    "ENFP": {
        "desc": "열정적이고 창의적인 성격의 활발한 활동가입니다.",
        "champions": [
            {"name": "Lux", "desc": "빛을 이용해 밝고 긍정적인 마법을 사용하는 소녀.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg"},
            {"name": "Nami", "desc": "바다의 힘으로 아군을 돕는 서포터.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nami_0.jpg"},
            {"name": "Rakan", "desc": "무대 위의 화려한 춤과 사랑으로 싸우는 챔피언.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rakan_0.jpg"}
        ]
    },
    "ISTJ": {
        "desc": "성실하고 책임감이 강한 관리자형입니다.",
        "champions": [
            {"name": "Shen", "desc": "균형을 지키기 위한 무결점의 닌자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Shen_0.jpg"},
            {"name": "Trundle", "desc": "힘과 규율로 상대를 지배하는 전사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Trundle_0.jpg"},
            {"name": "Sejuani", "desc": "냉혹한 겨울의 군단장.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sejuani_0.jpg"}
        ]
    },
    "ISFJ": {
        "desc": "온화하고 성실하며 배려심 깊은 수호자형입니다.",
        "champions": [
            {"name": "Braum", "desc": "강한 팔과 따뜻한 마음을 가진 설산의 수호자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Braum_0.jpg"},
            {"name": "Amumu", "desc": "안아줄 친구를 찾아 헤매는 외로운 미라.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Amumu_0.jpg"},
            {"name": "Sona", "desc": "말 대신 음악으로 감정을 전하는 서포터.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sona_0.jpg"}
        ]
    },
    "ESTJ": {
        "desc": "결단력 있고 리더십이 강한 경영자형입니다.",
        "champions": [
            {"name": "Leona", "desc": "태양의 힘으로 아군을 수호하는 전사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_0.jpg"},
            {"name": "Vi", "desc": "주먹으로 문제를 해결하는 법 집행자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vi_0.jpg"},
            {"name": "Poppy", "desc": "작지만 강한 망치의 기사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Poppy_0.jpg"}
        ]
    },
    "ESFJ": {
        "desc": "사교적이고 협동심 강한 집단 중심의 돌봄형입니다.",
        "champions": [
            {"name": "Lulu", "desc": "마법으로 모두를 웃게 만드는 요정 마법사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lulu_0.jpg"},
            {"name": "Morgana", "desc": "희생과 고뇌 속에서도 정의를 지키는 타락한 천사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Morgana_0.jpg"},
            {"name": "Janna", "desc": "바람처럼 부드럽게 아군을 지키는 수호신.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Janna_0.jpg"}
        ]
    },
    "ISTP": {
        "desc": "냉정하고 효율적인 실용주의자 유형입니다.",
        "champions": [
            {"name": "Zed", "desc": "그림자 속에서 처단하는 암살자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg"},
            {"name": "Kayn", "desc": "암흑과 정의의 갈림길에 선 그림자 전사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayn_0.jpg"},
            {"name": "Graves", "desc": "중후한 산탄총으로 전장을 누비는 무법자.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Graves_0.jpg"}
        ]
    },
    "ISFP": {
        "desc": "예술적이고 조용한 성격의 온순한 모험가입니다.",
        "champions": [
            {"name": "Ahri", "desc": "감성과 마법으로 매혹하는 여우.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg"},
            {"name": "Xayah", "desc": "반항심 가득한 자유로운 영혼의 전사.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Xayah_0.jpg"},
            {"name": "Seraphine", "desc": "음악으로 모두와 연결되는 꿈꾸는 가수.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Seraphine_0.jpg"}
        ]
    },
    "ESTP": {
        "desc": "모험을 즐기고 빠른 판단력이 뛰어난 활동가입니다.",
        "champions": [
            {"name": "Lee Sin", "desc": "몰입감 넘치는 전투 스타일의 무술가.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/LeeSin_0.jpg"},
            {"name": "Draven", "desc": "관심을 즐기는 화려한 도끼 쇼맨.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Draven_0.jpg"},
            {"name": "Samira", "desc": "스타일리시하게 적을 제거하는 거침없는 총잡이.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Samira_0.jpg"}
        ]
    },
    "ESFP": {
        "desc": "재미를 추구하고 감각적인 외향적 연예인형입니다.",
        "champions": [
            {"name": "Ezreal", "desc": "모험과 자유를 즐기는 매력적인 탐험가.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ezreal_0.jpg"},
            {"name": "Miss Fortune", "desc": "아찔한 매력과 총잡이의 카리스마.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_0.jpg"},
            {"name": "Fizz", "desc": "장난꾸러기 바다 요정.", "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fizz_0.jpg"}
        ]
    }
}

# Streamlit UI 구성
st.set_page_config(page_title="MBTI LoL 챔피언 추천", page_icon="🎮", layout="centered")
st.title("🧠 MBTI 기반 LoL 챔피언 추천")
st.write("당신의 MBTI에 맞는 리그 오브 레전드 챔피언 3명을 추천해드릴게요!")

mbti_options = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_options)

if selected_mbti:
    st.subheader(f"{selected_mbti} 유형")
    st.write(mbti_data[selected_mbti]["desc"])

    st.markdown("### 추천 챔피언들")
    for champ in mbti_data[selected_mbti]["champions"]:
        st.image(champ["img"], width=400, caption=champ["name"])
        st.write(f"**{champ['name']}**: {champ['desc']}")
