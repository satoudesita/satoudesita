import streamlit as st
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == "グー" and computer_choice == "チョキ") or \
         (user_choice == "チョキ" and computer_choice == "パー") or \
         (user_choice == "パー" and computer_choice == "グー"):
        return "勝ち"
    else:
        return "負け"

def main():
    st.title("じゃんけんゲーム")
    st.write("選んでください：")
    
    user_choice = st.radio("", ("グー", "チョキ", "パー"))
    computer_choice = random.choice(["グー", "チョキ", "パー"])
    
    st.write(f"あなたの選択: {user_choice}")
    st.write(f"コンピューターの選択: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    st.write(f"結果: {result}")

if __name__ == "__main__":
    main()
