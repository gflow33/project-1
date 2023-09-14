import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv('topics.csv')

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss", df['topic'])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from{user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""

    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email has been sent successfully")