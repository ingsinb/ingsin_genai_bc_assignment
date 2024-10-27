import streamlit as st
from logics.food_waste_query_handler import process_user_message
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.subheader("What would you like to know about food waste management? :apple:")
st.write("Your guide to food waste segregation and treatment.")
form = st.form(key="form")
user_prompt = form.text_area("Ask a question about food waste segregation or treatment. (e.g. What are the steps for food waste segregation?)")

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt)
    st.write(response)

    print(f"User Input is {user_prompt}")
