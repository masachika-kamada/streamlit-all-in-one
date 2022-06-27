import streamlit as st
import PyPDF2


"""
機能要求
1. PDFをアップロード
2. パスワード入力欄と実行ボタンが表示される
3. 実行ボタンで変換
4. 保存ボタンでファイルが保存される
※復号化によりロックが解除できない場合に、qpdfを使用することで
    パスワードを解除できるようにする記事があったが、
    デプロイすることを考えると微妙なので断念
"""


def run():
    file = st.file_uploader("翻訳したいpdfファイルをアップロードしてください", type=["pdf"])
    file_path = "./src.pdf"
    password = "MSFT2022"
    if file is not None:
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        remove_password(file_path, "dst.pdf", password)

        st.download_button(
            "ダウンロード",
            open("dst.pdf", "br"),
            file.name
        )


def remove_password(src_path, dst_path, src_password):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    src_pdf.decrypt(src_password)

    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)

    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)

    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)
