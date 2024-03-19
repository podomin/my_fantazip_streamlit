import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

st.image("./fantazip_logo.png")
st.title("🏠 안전한 동네 찾기 🏠 ")
st.warning("해당 데이터는 서울 법정동을 기준으로 하고 있습니다.")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("### 🤍'거주지역' 중심 지역  VS  '1인가구' 중심 지역")

st.markdown("🕵️‍♀️ : 조금 전에 'safe_county'에서 확인한 safe 지역은 '성동구, 성북구, 도봉구'였습니다. 그리고 cctv와 유흥주점 비율을 사용해서 범죄로부터 \
    safe한 지역을 파악할 수 있다는 검증을 완료했죠. 이제 이걸 활용해서 안전한 동네를 추리면 됩니다.")
st.markdown("🕵️‍♀️ : 하지만 문제가 있습니다! safe 지역 중에서 '성동구'를 중점적으로 살펴볼 예정이었는데, 아래 성동구의 1인가구 분포도를 좀 확인해보십시오.")
with st.expander(label=f"🔍 **1인 가구 분포도**"): 
    st.markdown("------------")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('##### 성동구 1인가구 분포도')
        st.image("./data/s_1인가구.png", width=300)
        df= pd.DataFrame({
                        '1인가구': '💙',
                        '2030 여성 1인가구': '🧡'}, index=['범례 색상'])
        st.dataframe(df)
        st.markdown("🕵️‍♀️ : 성동구는 안전하기는 하지만 1인 가구 수가 매우 적은 '거주중심지구'라는 것을 알 수 있습니다. \
            그러나 저희 분석 팀의 목적은 '2030 사회초년생을 위한 안전한 동네 추천'이라는 점을 기억하실 겁니다. 2030 사회초년생이 자취를 한다면, 대부분 1인 가구일 수밖에 없죠.\
            만약에 safe 지역인 성동구에서만 안전한 동네를 찾는다면, 본래의 분석 목적에서 살짝 벗어난 결과가 될 듯합니다. \
            그래서 지금까지의 인사이트를 토대로 1인가구 중심 지역에서도 추가로 안전한 동네를 찾기로 했습니다.")
        st.markdown("👉-👉-👉-👉-👉-👉-👉")
    with col2:
        st.markdown('##### 1인가구 분포도')
        st.markdown("🕵️‍♀️ : 이제, 모든 자치구 별 1인가구 분포도를 살펴본 후에 1인가구 중심지역을 선정하겠습니다. ")
        st.image("./data/1인가구.png", width=500)
        st.markdown("🕵️‍♀️ : 그래프를 보면 1위가 관악구, 2등이 강서구 순서로 1인가구가 많은 것을 확인할 수 있습니다.")
st.write(" ")
st.markdown("🕵️‍♀️ : 관악구 vs 강서구 둘 중 어디가 2030 사회초년생이 더 많이 거주하고 있을까요? 데이터로 확인해보시죠.")
with st.expander(label=f" 🔍 **관악구 vs 강서구**"): 
    st.markdown("------------")
    st.markdown("##### 인구 연령대 비교")
    st.image("./data/강서.png", width=500)
    st.image("./data/관악.png", width=500)
    st.markdown("🕵️‍♀️ : 확실히 관악구에는 20대 > 30대 , 강서구에는 20대 < 30대 많이 거주하는 것으로 보아, \
        강서구에 사회초년생 직장인이 더 많을 것이라고 추측할 수 있겠습니다. 이 추측도 아래에서 데이터로 확인해보겠습니다.")
    st.write(" ")
    st.write(" ")
    st.markdown("##### 취업 인구 수 비교")
    st.image("./data/관악강서.png", width=400)
    st.markdown(f"**(좌 - 우 : 자치구 이름, 2020년 3월, 2020년 4월, 2020년 5월 합계)**")
    st.markdown("🕵️‍♀️ : 자치구 별 취업인구 분포도를 살펴본 결과, \
        강서구에 2030 사회초년생 1인가구가 더 많다는 사실을 확실히 할 수 있었습니다. \
        그리고 강서구가 직장이 몰려있는 업무중심지구 (광화문, 여의도)와도 가까운 자치구임을 파악하여 1인가구 중심 지역으로 '강서구'를 선정하겠습니다. ")
    st.info(f"**1인가구 중심 지역 ➡️  강서구**")
st.write(" ")
st.markdown("##### ✔️'1인가구중심지구' - 강서구")
st.markdown("##### ✔️''거주중심지역' - 성동구")
st.info("🕵️‍♀️ Mission = 2030 사회초년생들이 자취하기 적합한 '1인가구중심지구' & 다양한 가구가 거주하고 있는 거주중심지역 \
    두 그룹으로 나눠서 안전한 동네 & 특징 파악하기")

    
st.write("  ")
st.markdown("-----------")
st.write("  ")


st.markdown("### 🤍거주중심지역 - 성동구 ")
st.markdown("#### step 01) cctv, 유흥주점 비율로 안전한 동네 찾기 ")
st.markdown("🕵️‍♀️ : safe 지역이면서 거주중심지역인 성동구에서 cctv, 유흥주점 비율을 활용해 안전한 동네를 추려보겠습니다.")
with st.expander(label=f"**< 2030 여성 인구 대비 cctv & 유흥주점 비율 >**"): 
    st.warning("▫️ safe (성동구, 성북구, 도봉구) 중에서 성동구가 위험 vs 안전 동네의 차이가 가장 크게 나타났기 때문에 주요 특징을 찾기에 좋을 듯하여 \
         ‘성동구’만을 집중적으로 분석을 진행했습니다. ")
    st.image("./data/filter_성동구.png", width=700)
    st.write("🕵️‍♀️ : cctv와 유흥주점의 비율이 둘 다 낮아야 안전한 동네라는 걸 기억하면서 그래프를 살펴보겠습니다.\
        cctv와 유흥주점 비율이 둘 다 낮은 곳은 상왕십리동이랑 하왕십리동으로 보이고 높은 곳은 홍익동이라는 점을 확인할 수 있습니다.")
    st.write("🕵️‍♀️ : 여기서 잠깐!!! 이상치로 보이는 도선동은 번외로 따로 살펴보도록 하겠습니다.")
st.markdown("##### < 결과 >")
st.markdown("🔴**위험 동네 - 홍익동,**  🟢**안전 동네 - 상왕십리동 & 하왕십리동**, 🟡**번외) - 도선동**")

st.write("")

st.markdown("#### step 02) 안전 VS 위험 동네 특징 파헤치기 ")
with st.expander(label=f"🟡 **도선동**"): 
    st.info("🕵️‍♀️ : 도선동은 왜 유흥주점 비율이 유독 높은 걸까요? ")
    
    if st.toggle("📊 도선동 인구 수 분포도 보기"):
        df= pd.DataFrame({
                        '1인가구': '💙',
                        '2030 여성 1인가구': '🧡'}, index=['범례 색상'])
        st.dataframe(df)
        image1 = Image.open('./data/도선동_인구.png')
        st.image(image1, width=300)
    st.write("🕵️‍♀️ : 평균을 나타내는 점선과 비교해 보면, 성동구 내에서도 도선동 인구 수가 적은 편인 점을 알 수 있습니다. \
        인구 수가 적어서 비율이 이상치였던 걸까...? 지역적인 특징이 있는 건 아닌지 지도에서도 살펴보도록 하겠습니다. ")
    
    if st.toggle("🗺️ 도선동 지도에서 살펴보기"):
        st.write('''[도선동 지도 링크](https://kko.to/7oJ7ui-8CO) ''', unsafe_allow_html=True)
    st.write("🕵️‍♀️ : 지도를 보면 도선동이 다른 동네와 특별히 다른 점이 있습니다. 동네 한 쪽에 여관이나 모텔이 모여있는 구역이 있었습니다. ")
    st.write(f"**<연령대 비율 파이차트>**")
    df= pd.DataFrame({
                    '19세이하': '💙',
                    '20~30 남성': '🧡',
                    '20~30 여성': '💚',
                    '40~60': '❤️',
                    '70~100': '💜'}, index=['범례 색상'])
    st.dataframe(df)
    st.image("./data/도선동_비교.png", width=700)
    st.info("🕵️‍♀️ : 오!! 또한 도선동 인구 연령대 중에서 2030 인구(🟧🟩) 비율이 높고 그 중에서 \
        2030 여성 인구(🟩) 비율이 눈에 띄게 높다는 점이 흥미롭습니다.\
        유독 유흥주점이 많은 곳은 숙박업소가 많고 2030 인구 비율이 높다고 볼 수 있을 것 같습니다.")
    
    
st.write("")

with st.expander(label=f"**🔴 홍익동  VS 🟢 상왕십리동, 하왕십리동**"): 
    st.info("🕵️‍♀️ : 위험한 동네와 안전한 동네는 어떠한 차이가 있을까요?")
    if st.toggle("📊 인구 수 분포도 (거주중심)"):
        image2 = Image.open('./data/s인구.png')
        st.image(image2,  width=700)
    st.write("🕵️‍♀️ : 하왕십리동에는 유독 인구 수가 굉장히 높다는 사실을 확인할 수 있습니다. ")
    
    if st.toggle("🗺️ 지도에서 살펴보기 (거주중심)"):
        st.write('''[홍익동 지도 링크](https://kko.to/ecFOX3dBv_) ''', unsafe_allow_html=True)
        st.write('''[상왕십리동 지도 링크](https://kko.to/LMKqbAHj4D) ''', unsafe_allow_html=True)
        st.write('''[하왕십리동 지도 링크](https://kko.to/up3SANQMqe) ''', unsafe_allow_html=True)
    st.write("🕵️‍♀️ : 지도 상에서 상왕십리동과 하왕십리동에는 홍익동과 비교했을 때, \
        아파트 단지가 굉장히 많다는 차이점이 있습니다. 바로 이어서, 인구 연령대 비율도 확인해보겠습니다.")
    st.write(f"**<연령대 비율 파이차트>**")
    df= pd.DataFrame({
                    '19세이하': '💙',
                    '20~30 남성': '🧡',
                    '20~30 여성': '💚',
                    '40~60': '❤️',
                    '70~100': '💜'}, index=['범례 색상'])
    st.dataframe(df)
    
    st.image("./data/s연령_pie.png", width=800)
    st.write("🕵️‍♀️ : 위험 동네와 비교했을 때, 안전한 동네는 19세 이하 비율이 더 높았고 \
        70~100세 비율이 낮다는 점이 흥미롭습니다.")
    st.write(" ")
    st.write(f"**<생활 & 거주 환경 조건 분포도>**")
    df= pd.DataFrame({
                    '버스역': '💙',
                    '지하철역': '🧡',
                    '도서관': '💚',
                    '공원': '❤️',
                    '유흥업소': '💜',
                    '경찰서': '🤎',
                    '여성안심지킴이집': '🩷'}, index=['위 그래프 범례 색상'])
    st.dataframe(df)
    st.image("./data/s_생활.png", width=700)
    st.image("./data/s_거주.png", width=700)
    df= pd.DataFrame({
                    'cctv': '💙',
                    '가로등/방범등': '🧡'}, index=['아래 그래프 범례 색상'])
    st.dataframe(df)
    st.info("🕵️‍♀️ :다양한 생활환경 조건들의 분포도를 확인해보니 거주중심지역에서의 \
        안전한 동네는 cctv 개수와 유흥업소가 적었습니다. 또한 안전한 동네는 교통 편리성이 좋았고\
        공원 or 도서관이 항상 하나씩은 있다는 사실을 확인했습니다.")

st.write("  ")

st.markdown("#### step 03) 안전 VS 위험 동네 특징 ✔️")
data = {
    '안전한 동네': ['아파트 단지 ⬆️', '교통 수단 ⬆️', '도서관 or 공원 ⬆️', '유흥업소 🔻','여성안심지킴이집 🔻', '0~19세 ⬆️'],
    '위험한 동네': ['cctv ⬆️', '유흥업소 ⬆️', '여성안심지킴이집 ⬆️', '인구 수 🔻', '70~100 ⬆️',' ']
}
df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("#### step 04) 거주중심지역의 안전한 동네는...?? ")
col1, col2 = st.columns(2)
with col1:
    st.info(f"**🎉상왕십리동🎉**")
    
with col2:
    st.info(f"**🎊 하왕십리동 🎊**")   


st.write("  ")
st.markdown("-----------")
st.write("  ")

st.markdown("### 🤍1인가구중심지역 - 강서구 ")
st.markdown("#### step 01) cctv, 유흥주점 비율로 안전한 동네 찾기 ")
st.markdown("🕵️‍♀️ : 이번에는 1인가구중심지역 강서구에서 cctv, 유흥주점 비율을 활용해 안전한 동네를 추려보겠습니다.")
with st.expander(label=f"**< 2030 여성 인구 대비 cctv & 유흥주점 비율 >**"): 
    st.image("./data/filter_강서구.png", width=700)
    st.write("🕵️‍♀️ : cctv와 유흥주점의 비율이 둘 다 낮아야 안전한 동네라는 걸 기억하면서 그래프를 살펴본 결과,\
        cctv와 유흥주점 비율이 매우 낮은 곳은 등촌동과 염창동이며 둘 다 높은 곳은 공항동이라는 점을 확인했습니다.")
    st.write("🕵️‍♀️ : 여기서 잠깐!!! cctv 비율 그래프에서 이상치로 보이는 개화동은 번외로 따로 살펴보도록 하겠습니다.")
st.markdown("##### < 결과 >")
st.markdown("🔴**위험 동네 - 공항동**   🟢**안전 동네 - 등촌동,  염창동**🟡**번외) - 개화동**")

st.write("")

st.markdown("#### step 02) 안전 VS 위험 동네 특징 파헤치기 ")
with st.expander(label=f"🟡 **개화동**"): 
    st.info("🕵️‍♀️ : 개화동은 왜 cctv 비율이 유독 높은 걸까? ")
    
    if st.toggle("📊 개화동 인구 수 분포도 보기"):
        df= pd.DataFrame({
                        '1인가구': '💙',
                        '2030 여성 1인가구': '🧡'}, index=['변수 색상'])
        st.dataframe(df)
        image1 = Image.open('./data/개화동_인구.png')
        st.image(image1, width=300)
    st.write("🕵️‍♀️ : 점선(평균)과 비교해 봤을 때, 개화동에 거주하는 인구 수가 압도적으로 낮다는 것을 확인했습니다.  \
        인구 수가 적어서 cctv 비율이 이상치 수준으로 높게 나왔던 것 같습니다. \
        추가로 지역적인 특성을 살펴보면서 인구 부족 현상에 대해 파헤쳐보겠습니다. ")
    
    if st.toggle("🗺️ 개화동 지도에서 살펴보기"):
        st.write('''[개화동 지도 링크](https://kko.to/K0R5Qh2d0W) ''', unsafe_allow_html=True)
    st.write("🕵️‍♀️ : 지도를 보면 개화동은 면적은 넓지만 산, 농장, 한강, 공원 등이 대부분의 \
        면적을 차지하여 사람이 살 만한 공간이 없다는 것을 알 수 있습니다. ")
    st.info("🕵️‍♀️ : 아하! 개화동은 면적은 넓지만 거주민이 너무 적어서 cctv 비율이 유독 높게 나왔다는 것을 확인했습니다. ")
    
    
st.write("")

with st.expander(label=f"**🔴 공항동  VS 🟢 등촌동, 염창동**"): 
    st.info("🕵️‍♀️ : 위험한 동네와 안전한 동네는 어떠한 차이가 있을까?")
    if st.toggle("📊 인구 수 분포도 (1인가구중심)"):
        image2 = Image.open('./data/g_인구.png')
        st.image(image2,  width=700)
    st.write("🕵️‍♀️ : 인구 수가 등촌동 > 염창동 > 공항동 순으로 높은 것을 확인했습니다. ")
    
    if st.toggle("🗺️ 지도에서 살펴보기 (1인가구중심)"):
        st.write('''[홍익동 지도 링크](https://kko.to/UoAod4a3gZ) ''', unsafe_allow_html=True)
        st.write('''[등촌동 지도 링크](https://kko.to/Txw6RtLh0t) ''', unsafe_allow_html=True)
        st.write('''[염창동 지도 링크](https://kko.to/PVUmIiAoel) ''', unsafe_allow_html=True)
    st.write("🕵️‍♀️ : 지도를 보면 등촌동과 염창동은 아파트 단지와 학교가 많이 있다는 것을 볼 수 있습니다.  \
        반면에, 공항동은 면적 절반이 김포공항이었고 그 옆에 빌라와 주택이 모여있다는 사실을 확인했습니다.")
    st.write(f"**<연령대 비율 파이차트>**")
    df= pd.DataFrame({
                    '19세이하': '💙',
                    '20~30 남성': '🧡',
                    '20~30 여성': '💚',
                    '40~60': '❤️',
                    '70~100': '💜'}, index=['범례 색상'])
    st.dataframe(df)
    st.image("./data/g_인구pie.png", width=800)
    st.write("🕵️‍♀️ : 등촌동과 염창동은 전체적으로 인구가 많고 특히 아이들의 비율이 높습니다. 2030세대 중에서 여성의 비율이 > 남성보다 더 높은 점도 흥미롭습니다.")
    st.write("반면에, 공항동은 인구가 적었으며 4060세대의 비율이 높고 2030세대 중에서는 남성 비율이 > 여성보다 높습니다.")
             
    st.write(f"**<생활 & 거주 환경 조건 분포도>**")    
    df= pd.DataFrame({
                    '버스역': '💙',
                    '지하철역': '🧡',
                    '도서관': '💚',
                    '공원': '❤️',
                    '유흥업소': '💜',
                    '경찰서': '🤎',
                    '여성안심지킴이집': '🩷'}, index=['위 그래프 범례 색상'])
    st.dataframe(df)
    st.image("./data/g_생활.png", width=700)
    st.image("./data/g_거주.png", width=700)
    df= pd.DataFrame({
                    'cctv': '💙',
                    '가로등/방범등': '🧡'}, index=['아래 그래프 범례색상'])
    st.dataframe(df)
    st.info("🕵️‍♀️ : 1인가구 중심 지역인 강서구의 안전한 동네는 도서관 or 공원이 많았고 유흥주점도 조금씩 있지만 적은 편이었습니다.\
        반면에, 위험한 동네는 유흥주점 많고 교통 편리성이 좋았는데 공항 근처라는 점을 고려해 특징에서 제외하겠습니다.")

st.write("  ")

st.markdown("#### step 03) 안전 VS 위험 동네 특징 ✔️")
data = {
    '안전한 동네': ['아파트 단지 ⬆️', '도서관 or 공원 ⬆️', '유흥업소 🔻', '인구 수 ⬆️', '0~19세 ⬆️', ' 여성2030⬆️ '],
    '위험한 동네': ['도서관 or 공원 🔻', '유흥업소 ⬆️', '인구 수 🔻', '4060세 ⬆️ ',' 남성2030⬆️ ',' ']
}
df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("#### step 04) 1인가구중심지역의 안전한 동네는...?? ")
col1, col2 = st.columns(2)
with col1:
    st.info(f"**🎉등촌동🎉**")
    
with col2:
    st.info(f"**🎊 염창동 🎊**")  
    
st.write(" ")
st.markdown('-------')
st.write(" ")

st.markdown("#### 🤍한 단계 더 들어가기")
st.write("🕵️‍♀️ : 안전한 거주지역 + 1인가구가 많은 지역에서 추출한 안전한 동네는 대부분 아파트 단지가 꽤 있는 편이었습니다. \
    그리고 아이들 인구가 조금 더 많은 사실을 통해 1인가구 보다는 가족 단위의 가구들이 많은 편이라고 추측해볼 수 있습니다. \
    그래서 지금까지 나온 결론이 분석팀의 타겟층에 찰떡같이 들어 맞는다고 보기는 힘들 것 같아 조금 아쉽습니다.")
st.markdown("🕵️‍♀️ : 그리하여 한 단계 더 나아가보겠습니다!! 1인 가구 수가 확실하게 많은 동네를 추려서 그 중에서의 안전한 동네도 보너스로 살펴보겠습니다.")
