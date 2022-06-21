import streamlit as st


def sidebar():
    with st.sidebar:
        func_select = st.radio(
            "機能切替",
            ("PDFを画像に変換", "画像をリサイズ", "画像サイズの表示")
        )

    return func_select


def main():
    st.markdown('# Image Process all in one')
    func = sidebar()

    if func == "PDFを画像に変換":
        pass
    elif func == "画像をリサイズ":
        pass
    elif func == "画像サイズの表示":
        pass


if __name__ == '__main__':
    main()
