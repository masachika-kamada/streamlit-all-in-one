import numpy as np
import streamlit as st

"""
機能要求
1. スライダーでRGBの値を入力する
2. 色が表示される
"""


def run():
    r = st.slider("R", 0, 255, 0)
    g = st.slider("G", 0, 255, 0)
    b = st.slider("B", 0, 255, 0)

    st.markdown(f"## RGB: {r}, {g}, {b}")

    color = np.full((300, 800, 3), (b, g, r), dtype=np.uint8)
    st.image(color)
