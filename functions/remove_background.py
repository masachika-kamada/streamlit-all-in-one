import streamlit as st
from rembg import remove
from PIL import Image

"""
機能要求
1. 画像をアップロード
2. 実行ボタンで背景を透過
3. ダウンロードボタンが表示される
4. ボタンを押すと画像がダウンロードされる
"""


def run():
    file = st.file_uploader("画像をアップロードしてください", type=["jpg", "png"])
    input_path = "./src.png"
    output_path = "./output.png"
    if file is not None:
        with open(input_path, "wb") as f:
            f.write(file.getvalue())
        
        img = Image.open(input_path)
        st.image(img, caption="Uploaded Image.", use_column_width=True)

        # 実行ボタンを押したら処理が始まる
        if st.button("実行"):
            result = remove(img)
            result.save(output_path)

            dst = Image.open(output_path)
            st.image(dst, caption="Output Image.", use_column_width=True)

            st.download_button(
                "ダウンロード",
                open(output_path, "br"),
                file.name.replace(".jpg", ".png"),
            )
