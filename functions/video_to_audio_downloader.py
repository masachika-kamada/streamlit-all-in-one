import streamlit as st
import ffmpeg


"""
機能要求
1. mp4ファイルをアップロード
2. 保存ボタンを押す
3. mp3ファイルが保存される
"""


def run():
    file = st.file_uploader("mp4ファイルをアップロードしてください", type=["mp4"])
    file_path = "./src.mp4"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        stream = ffmpeg.input(file_path)
        stream = ffmpeg.output(stream, "dst.mp3")
        ffmpeg.run(stream)

        st.download_button(
            "ダウンロード",
            open("dst.mp3", "br"),
            file.name.replace("mp4", "mp3")
        )
