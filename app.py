import streamlit as st
from functions import pdf_to_image_downloader
from functions import video_to_audio_downloader
from functions import password_maker
from functions import qrcode_maker
from functions import color_palette
from functions import youtube_download
from functions import resize_image
from functions import remove_background
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
             "画像の背景削除",
             "トリミング・余白追加",  # 正方形ロゴ作成
             "画像をリサイズ",
             "画像サイズの表示")
        )

    return func_select


def main():
    st.markdown("# Image Process all in one")
    func = sidebar()

    match func:
        case "PDFを画像に変換":
            pdf_to_image_downloader.run()
        case "動画を音声に変換":
            video_to_audio_downloader.run()
        case "パスワード生成":
            password_maker.run()
        case "QRコード生成":
            qrcode_maker.run()
        case "カラーパレット":
            color_palette.run()
        case "YouTubeダウンロード":
            youtube_download.run()
        case "画像の背景削除":
            remove_background.run()
        case "画像をリサイズ":
            resize_image.run()
        # case "PDFのパスワード解除":
        #     unlock_pdf.run()
        case "画像サイズの表示":
            pass


if __name__ == "__main__":
    main()
