import streamlit as st
import cv2

"""
機能要求
1. 画像をアップロード
2. 割合でリサイズと固定サイズでリサイズを選択
3. リサイズボタンを押す
4. ダウンロードボタンが表示される
5. ボタンを押すと画像がダウンロードされる
"""


def run():
    file = st.file_uploader("画像をアップロードしてください", type=["jpg", "png"])
    file_path = "./src.png"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())
        
        img = cv2.imread(file_path)
        h, w = img.shape[:2]
        st.image(img, caption='Uploaded Image.', use_column_width=True)

        # トグルボタンでリサイズの方法を選択
        resize_type = st.radio("リサイズの方法を選択してください", ("割合でリサイズ", "固定サイズでリサイズ"))

        if resize_type == "割合でリサイズ":
            resize_rate = st.number_input("リサイズの割合を入力してください", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
            if st.button("リサイズ"):
                img = cv2.resize(img, (int(w * resize_rate), int(h * resize_rate)))
                cv2.imwrite(file_path, img)
                st.download_button(
                    "ダウンロード",
                    open(file_path, "br"),
                    file.name
                )

        else:
            resize_w = st.number_input("リサイズ後の 幅 を入力してください", min_value=1, max_value=4000, value=100, step=1)
            resize_h = st.number_input("リサイズ後の 高さ を入力してください", min_value=1, max_value=4000, value=100, step=1)
            if st.button("リサイズ"):
                img = cv2.resize(img, (resize_w, resize_h))
                cv2.imwrite(file_path, img)
                st.download_button(
                    "ダウンロード",
                    open(file_path, "br"),
                    file.name
                )
