import streamlit as st
from functions import pdf_to_image_downloader
from functions import video_to_audio_downloader
from functions import password_maker
from functions import qrcode_maker
from functions import color_palette
from functions import youtube_download
from functions import resize_image
# import unlock_pdf


def sidebar():
    with st.sidebar:
        func_select = st.radio(
            "機能切替",
            ("PDFを画像に変換",
             "動画を音声に変換",
             # "PDFのパスワード解除",
             "パスワード生成",
             "QRコード生成",
             "カラーパレット",
             "YouTubeダウンロード",
             "トリミング・余白追加",  # 正方形ロゴ作成
             "画像をリサイズ",
             "画像サイズの表示")
        )

    return func_select


def main():
    st.markdown("# Image Process all in one")
    func = sidebar()

    if func == "PDFを画像に変換":
        pdf_to_image_downloader.run()
    elif func == "動画を音声に変換":
        video_to_audio_downloader.run()
    elif func == "パスワード生成":
        password_maker.run()
    elif func == "QRコード生成":
        qrcode_maker.run()
    elif func == "カラーパレット":
        color_palette.run()
    elif func == "YouTubeダウンロード":
        youtube_download.run()
    elif func == "画像をリサイズ":
        resize_image.run()
    # elif func == "PDFのパスワード解除":
    #     unlock_pdf.run()
    elif func == "画像サイズの表示":
        pass


if __name__ == "__main__":
    main()
