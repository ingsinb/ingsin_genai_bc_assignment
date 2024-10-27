import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="SG BinBuddy"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("SG BinBuddy: Your Guide to Manage Waste and Recycle Right")
st.image("./img/earth.png")

st.subheader("About Us")
proj_scope_obj = """
**Project Scope**\n
As Singapore faces more challenges in waste management, addressing the alarming trends surrounding food waste and recycling becomes crucial.\n
In Singapore, food waste accounted for around 11% of the total waste generated in 2023 and the overall recycling rate has declined from 62% in 2013 to 52% in 2023. These facts highlight an urgent need for improved waste management strategies.\n
Hence, SG BinBuddy application aims to develop an interactive chat platform to help Singaporeans to understand food waste management and best practices of recycling.

**Objectives**\n
*Educational Awareness*\n
Increase awareness about food waste and recycling practices among Singaporeans through engaging chatbot interface where users can post questions on food wastage management and the classification of their items. \n
This includes enhancing knowledge on the raw materials of the items to be recycle so Singaporeans has the knowledge of raw materials that make up common household items and their recyclability.\n

*Behavorial Change*\n
Provide practical tips on waste management to encourage users to develop consistent wasta management practices.


"""
st.write(proj_scope_obj)

data_sources = """
**Data Sources**\n

- Recycling Guide from NEA: https://www.cgs.gov.sg/files/Recycle%20Right/recycling_guide_final.pdf
- Food waste segregation and management guide from NEA: https://www.nea.gov.sg/docs/default-source/envision/food-waste/nea-fw-segregation-and-treatment-guidebook.pdf
"""

st.markdown(data_sources)

key_features = """
**Key Features**\n

:apple: Wastage Food Guru: The chatbot understand and respond to user enquiry on food wastage segregation and treatment.\n
:recycle: Smart Recycle Item Checker: offers a user-friendly interface that allows users to input the item that they wish to recycle and verify whether the item is recycable. The chatbot also provides recycling tips and guidelines such as the raw material of the item as well as the disposal methods of both recyclable and non-recyclable items.\n\n
"""

st.write(key_features)

with st.expander("See disclaimer"):
    st.write("""IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.""")