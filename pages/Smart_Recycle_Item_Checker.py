import streamlit as st
from logics.recycle_item_query_handler import process_user_message
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()


st.subheader("What item do you want to recycle today? :recycle:")
st.write("Your guide to recycling right.")

form = st.form(key="form")
user_prompt = form.text_area("Type your item here (e.g. newspaper, drinking straw) to verify if it should be recycled.")

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt)
    st.write(response)
    print(f"User Input is {user_prompt}")

