import streamlit as st
st.title("bmi診断")
st.html("""
    <p style="color:red; font-size:30px;">元気になろう！！</p>
    <img src="https://d3cmdai71kklhc.cloudfront.net/post_watermark/contest/104963/ct_20201108-200339480_pudwd.jpg">
                """)
st.text("体重を入力してください")
a=st.number_input("体重")
st.text("身長を入力してください")
b=st.number_input("身長(m)")

if st.button("計算"):
    c=a/b**2
    st.write(c)
