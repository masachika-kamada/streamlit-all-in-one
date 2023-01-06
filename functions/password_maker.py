import secrets
import string

import streamlit as st

"""
機能要求
1. 使用できる文字をチェックボックスで選択
2. 文字数選択
3. 生成ボタンを押す
4. パスワードが表示される
5. パスワードをコピーするボタンを押す
"""


def run():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    use_lower = st.checkbox("小文字", value=True)
    use_upper = st.checkbox("大文字", value=True)
    use_numbers = st.checkbox("数字", value=True)
    use_symbols = st.checkbox("記号", value=True)

    # 記号に使用する文字をテキストボックスで編集
    if use_symbols:
        placeholder = st.empty()
        symbols = placeholder.text_input("記号", value=symbols, key="symbols")
        if len(symbols) == 0 or st.button("記号をリセット"):
            symbols = string.punctuation
            placeholder.text_input("記号", value=symbols)

    # パスワードの文字数
    password_length = st.slider(
        label="パスワードの文字数",
        min_value=8,
        max_value=32,
        value=16,
        step=1
    )

    make_password = st.button("生成")

    # チェックを付けた種類の文字を1文字以上含むようにする
    if make_password:
        if not (use_lower or use_upper or use_numbers or use_symbols):
            st.error("1つ以上の文字を選択してください")
            return

        characters = ""
        if use_lower:
            characters += lower
        if use_upper:
            characters += upper
        if use_numbers:
            characters += numbers
        if use_symbols:
            characters += symbols

        # チェックボックスで選択した種類の文字が全て含まれるように、含まれなかった場合は再度生成する
        while True:
            password = "".join(secrets.choice(characters) for i in range(password_length))
            if use_lower and not any(c in lower for c in password):
                continue
            if use_upper and not any(c in upper for c in password):
                continue
            if use_numbers and not any(c in numbers for c in password):
                continue
            if use_symbols and not any(c in symbols for c in password):
                continue
            break

        st.code(password, language="plaintext")
