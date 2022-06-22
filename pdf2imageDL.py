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
    file = st.file_uploader("翻訳したいpdfファイルをアップロードしてください", type=["pdf"])
    file_path = "./src.pdf"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        images = pdf2image.convert_from_path(
            file_path,
            poppler_path="C:/poppler-22.01.0/Library/bin",
            dpi=200,
            fmt="jpg")

        if len(images) == 1:
            image = images[0]
            w, h = image.size
            target_height = 450
            width = int(target_height / h * w)
            st.image(image, width=width)
            image.save("dst.png")

            st.download_button(
                "ダウンロード",
                open("dst.png", "br"),
                file.name.replace("pdf", "jpg")
            )

        else:
            isall = st.checkbox(label="全選択")
            checkbox = []
            yoko = 3
            for y in range(-(-len(images) // yoko)):
                cols = st.columns(yoko)
                for x in range(yoko):
                    idx = y * yoko + x
                    if idx >= len(images):
                        break
                    with cols[x]:
                        st.image(images[idx])
                        checkbox.append(st.checkbox(f"ページ{idx + 1}", value=isall))

            print(checkbox)
