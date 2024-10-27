import streamlit as st

st.subheader("Methodology")
st.write("**Smart Recycle Item Checker**")

st.image("./img/ma_recyclable_checker.png")

checker_method = """
The program will break down the checking of the item in smaller steps for LLM. Following are the main steps:
- Step 1: Data preparation \n
This includes loading and preprocess the data of recycling classification guidelines (e.g. product, raw material, recycle action to be taken) that is stored in a CSV file.\n
- Step 2: Query Categorization \n
This step will help to categorize incoming user queries. This function provides more details on what are the likely items the user mentions in the query and the relevant raw materials.\n
- Step 3: Item Information Retrieval \n
Based on the query categorization, this step will retrieve the other relevant item information from the data. This includes the decision of whether to recycle the item and the action to be taken to dispose/recycle the item.\n
- Step 4: LLM Reponse Output \n
In this step, LLM will generate response based on the necessary information gathered in Multi-Action prompting technique. \n
Firstly, the LLM is prompted to understand the products retrieve from Step 3. Next, the LLM is prompted to generate response based on the item in user's query. Lastly, the LLM is prompted to output the response in an informative and detailed manner that can provide the user with all the information he/she needs.\n
The LLM is also to output in a specific manner:\n
    **Recyclable**:Yes/No\n
    **Material**:\n
    **Action that can be taken**:
"""
st.write(checker_method)

st.write("**Wastage Food Guru**")
st.image("./img/rag_food_waste_management.png")

rag_method = """
The program will leverage on Retrieval-Augmented Generation (RAG) to output response. Following are the main steps:
- Step 1: Document Loading\n
This step is to load and prepare the document of food wastage management in PDF for further processing in next step.\n
- Step 2: Splitting & Chunking \n
The text from document is split into smaller chunks or segments which are to be the building blocks for next steps.\n
- Step 3: Storage \n
The embeddings of these chunks or segments are created and stored in a Chroma vector store.
- Step 4: Retrieval \n
The system retrieves the relevant chunks from the vector store based on the user query. This step is critical to ensure the system retrieve the most relevant and critical information from the document.
- Step 5: LLM Reponse Output  \n
In this step, the LLM generates a coherent and concise response based on the defined prompts and relevant chunks
"""
st.write(rag_method)