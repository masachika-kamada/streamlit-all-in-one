from yt_dlp import YoutubeDL
import streamlit as st
import os
import glob

"""
機能要求
1. URLを入力する
2. ダウンロードボタンを押す
3. ダウンロードされる
"""


def run():
    url = st.text_input("URLを入力してください")

    confirmation = st.button("URLを確定")

    if confirmation:
        # *.mp4がすでにある場合は削除する
        for file in glob.glob("*.mp4"):
            os.remove(file)

        ydl_opts = {"format": "best"}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        video_name = glob.glob("*.mp4")[0]
        print(video_name)

        st.download_button(
            "ダウンロード",
            open(video_name, "br"),
            video_name
        )
        
