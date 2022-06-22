import streamlit as st
import pdf2image


"""
機能要求
1. PDFをアップロード
2. プレビュー画像が表示される
3. ページを選択する（全選択もつける）
4. 保存ボタンを押す
5. 1ページのみの時はJPGファイルが保存される
6. 複数ページの時はZIPファイルが保存される
"""


def run():
    file = st.file_uploader("翻訳したいpdfファイルをアップロードしてください", type=['pdf'])
    file_path = "./src.pdf"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        run = st.button("画像をダウンロード")

        images = pdf2image.convert_from_path(
            file_path,
            poppler_path="C:/poppler-22.01.0/Library/bin",
            dpi=200,
            fmt='jpg')

        if len(images) == 1:
            w, h = images[0].size
            target_height = 450
            width = int(target_height / h * w)
            st.image(images[0], width=width)

        else:
            cols = st.columns(len(images))
            for i in range(len(images)):
                with cols[i]:
                    st.image(images[i])
                    st.checkbox(f"ページ{i + 1}", value=True)
