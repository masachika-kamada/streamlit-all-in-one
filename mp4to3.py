import streamlit as st
import ffmpeg

mp4_path = "D:/music/tomorrow moroha.mp4"
stream = ffmpeg.input(mp4_path)
stream = ffmpeg.output(stream, "test.mp3")
ffmpeg.run(stream)


"""
機能要求
1. mp4ファイルをアップロード
2. 保存ボタンを押す
3. mp3ファイルが保存される
"""


def run():
    file = st.file_uploader("pdfファイルをアップロードしてください", type=["mp4"])
    file_path = "./src.mp4"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        stream = ffmpeg.input(mp4_path)
        stream = ffmpeg.output(stream, "test.mp3")
        ffmpeg.run(stream)

        st.download_button(
            "ダウンロード",
            open("dst.jpg", "br"),
            file.name.replace("pdf", "jpg")
        )
