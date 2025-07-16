import streamlit as st
import pandas as pd
import altair as alt

# CSV 파일 불러오기 (같은 폴더에 있다고 가정)
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

# 데이터 로드
df = load_data()

st.set_page_config(page_title="국가별 MBTI 시각화", page_icon="🌐", layout="centered")
st.title("🌍 국가별 MBTI 유형 분석")
st.markdown("국가를 선택하면, 해당 국가에서 가장 흔한 상위 3개 MBTI 유형을 보여줍니다.")

# 국가 선택
countries = df['Country'].unique()
selected_country = st.selectbox("국가를 선택하세요:", sorted(countries))

# 선택한 국가 데이터에서 MBTI 비율 추출
country_data = df[df['Country'] == selected_country].iloc[0]
mbti_scores = country_data.drop(labels="Country")

# 상위 3개 MBTI 추출
top_mbti = mbti_scores.sort_values(ascending=False).head(3).reset_index()
top_mbti.columns = ['MBTI', 'Proportion']

# Altair 차트 생성
chart = alt.Chart(top_mbti).mark_bar(color="#5b9bd5").encode(
    x=alt.X('MBTI', sort='-y'),
    y=alt.Y('Proportion', title='비율'),
    tooltip=['MBTI', 'Proportion']
).properties(
    title=f"📊 {selected_country}의 상위 3개 MBTI 유형",
    width=500,
    height=400
)

# 차트 출력
st.altair_chart(chart, use_container_width=True)

# 표로도 함께 보여줌
with st.expander("🔍 MBTI 데이터 확인"):
    st.dataframe(top_mbti)
