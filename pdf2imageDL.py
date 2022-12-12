import os
import shutil
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
    file = st.file_uploader("pdfファイルをアップロードしてください", type=["pdf"])
    file_path = "./src.pdf"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        images = pdf2image.convert_from_path(
            file_path,
            poppler_path="./poppler-bin",
            dpi=200,
            fmt="jpg")

        checkbox = []

        if len(images) == 1:
            image = images[0]
            w, h = image.size
            target_height = 450
            width = int(target_height / h * w)
            st.image(image, width=width)
            image.save("dst.jpg")

            st.download_button(
                "ダウンロード",
                open("dst.jpg", "br"),
                file.name.replace("pdf", "jpg")
            )

        else:
            cols_head = st.columns(3)
            with cols_head[0]:
                isall = st.checkbox(label="全選択")
            with cols_head[1]:
                make_output_file = st.button("選択確定")

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
            if make_output_file is True and True in checkbox:
                idx = [i for i, x in enumerate(checkbox) if x is True]
                print(idx)
                with cols_head[2]:
                    if len(idx) == 1:
                        images[idx[0]].save("dst.jpg")
                        st.download_button(
                            "ダウンロード",
                            open("dst.jpg", "br"),
                            file.name.replace("pdf", "jpg")
                        )
                    else:
                        os.makedirs("out", exist_ok=True)
                        for i in idx:
                            images[i].save(f"out/page{i + 1}.jpg")
                        shutil.make_archive("out", format="zip", root_dir="out")
                        st.download_button(
                            "ダウンロード",
                            open("out.zip", "br"),
                            file.name.replace("pdf", "zip")
                        )
