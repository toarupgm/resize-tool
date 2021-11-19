import streamlit as st
from PIL import Image
import numpy as np
st.title("リサイズツール")

uploaded_file = st.file_uploader('Choose a image file')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    resultimg = image
    st.image(
        image, caption='upload image',
        use_column_width=True
    )
    min_value = 2
    max_value = int((image.height + image.width)/10)
    slider = st.slider("リサイズ", min_value, max_value, max_value, 2)
    slider = slider/10
    resultimg = resultimg.resize((int(image.width/slider), int(image.height/slider)), Image.LANCZOS)

    st.image(
        resultimg, caption='result image',
        use_column_width=True
    )
