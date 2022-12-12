import streamlit as st
from functions import pdf_to_image_downloader
from functions import video_to_audio_downloader
# import unlock_pdf


def sidebar():
    with st.sidebar:
        func_select = st.radio(
            "機能切替",
            ("PDFを画像に変換",
             "動画を音声に変換",
             # "PDFのパスワード解除",
             "画像をリサイズ",
             "画像サイズの表示")
        )

    return func_select


def main():
    st.markdown('# Image Process all in one')
    func = sidebar()

    if func == "PDFを画像に変換":
        pdf_to_image_downloader.run()
    elif func == "動画を音声に変換":
        video_to_audio_downloader.run()
    elif func == "画像をリサイズ":
        pass
    # elif func == "PDFのパスワード解除":
    #     unlock_pdf.run()
    elif func == "画像サイズの表示":
        pass


if __name__ == '__main__':
    main()
