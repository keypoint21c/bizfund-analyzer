import streamlit as st
from PIL import Image
from ocr import extract_text
from analyzer import parse_business_info, recommend_funds

st.title("사업자 자금 추천 분석기")

uploaded_file = st.file_uploader(
    "사업자등록증 업로드", type=["png","jpg","jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="업로드된 사업자등록증")

    text = extract_text(image)

    st.subheader("OCR 추출 텍스트")
    st.text(text)

    info = parse_business_info(text)

    st.subheader("사업자 정보")

    st.write(info)

    funds = recommend_funds(info)

    st.subheader("추천 정책자금")

    for f in funds:
        st.write(f["name"])
        st.write(f["site"])
