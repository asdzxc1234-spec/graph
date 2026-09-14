import streamlit as st
import pandas as pd
import plotly.express as px


# 페이지 설정
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    page_icon="🎬",
    layout="wide",
)

# 제목
st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

# 데이터 불러오기
DATA_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"
)

df = pd.read_csv(DATA_URL)

# 장르 처리
# 여러 장르가 세로막대(|)로 구분된 경우 첫 번째 장르만 사용
df["genre_first"] = (
    df["genre"]
    .fillna("미분류")
    .astype(str)
    .str.split("|")
    .str[0]
    .str.strip()
)

# 장르별 영화 편수
genre_counts = (
    df["genre_first"]
    .value_counts()
    .rename_axis("장르")
    .reset_index(name="영화 편수")
)

# 그래프 영역
st.subheader("1. 장르별 영화 편수")

fig = px.pie(
    genre_counts,
    names="장르",
    values="영화 편수",
    hole=0.5,
    title="장르별 영화 편수",
)

fig.update_traces(
    textinfo="percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "영화 편수: %{value}편<br>"
        "비율: %{percent}<extra></extra>"
    ),
)

fig.update_layout(
    legend_title_text="장르",
    margin=dict(t=60, b=20, l=20, r=20),
)

st.plotly_chart(fig, use_container_width=True)

# 그래프로 알 수 있는 것
st.markdown("---")
st.markdown("### 이 그래프로 알 수 있는 것")
st.info("여기에 이 그래프에서 발견한 특징을 한 문장으로 적어 보세요.")
st.markdown("---")
