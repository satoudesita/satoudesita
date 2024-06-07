
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="歴史問題ガチャ")

# タイトルと説明
st.title('歴史問題単語ガチャ')

st.write('歴史の問題をランダムに表示して、勉強をサポートします！')
st.write('がんばってください！')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("zyouhou.xlsx")

words_df = load_data()

st.write(load_data)


# ガチャ機能
if st.button('ガチャを引く！'):
    rarity_probs = {
        'N': 0.4,
        'R': 0.3,
        'SR': 0.2,
        'SSR': 0.1
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))
    subset_df = words_df[words_df['レア度'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"問題: {st.session_state.selected_word['問題']}")
    st.subheader(f"レア度: {st.session_state.selected_word['レア度']}")

    # 意味を確認するボタンを追加
    if st.button('解答を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"解答: {st.session_state.selected_word['解答']}")

        


st.set_page_config(page_title="英語単語ガチャ")

# タイトルと説明
st.title('英語単語ガチャ')

st.write('英語単語の問題をランダムに表示して、勉強をサポートします！')
st.write('がんばってください！')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("eigo.xlsx")

words_df = load_data()

st.write(load_data)


# ガチャ機能
if st.button('ガチャを引く！'):
    rarity_probs = {
        'N': 1.0,
        
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))
    subset_df = words_df[words_df['レア度'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"問題: {st.session_state.selected_word['問題']}")
    st.subheader(f"レア度: {st.session_state.selected_word['レア度']}")

    # 意味を確認するボタンを追加
    if st.button('解答を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"解答: {st.session_state.selected_word['解答']}")