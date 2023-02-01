import pyqrcode

import streamlit as st

"""
機能要求
1. テキストボックスに文字列を入力する
2. 生成ボタンを押す
3. QRコードが表示される
4. ダウンロードボタンを押すと画像をダウンロード
"""


def run():
    text = st.text_input("QRコードにしたい文字列を入力してください")
    scale = st.slider("QRコードのサイズ", 1, 10, 5)

    make_qrcode = st.button("生成")

    if make_qrcode and text != "":
        qrcode = pyqrcode.create(text)
        qrcode.png("qrcode.png", scale=scale)
        st.image("qrcode.png")
        st.download_button(
            "ダウンロード",
            open("qrcode.png", "br"),
            "qrcode.png"
        )
