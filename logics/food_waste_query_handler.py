from langchain_community.document_loaders import PyPDFLoader
from helper_functions import llm
from langchain.prompts import PromptTemplate


# load the PDF file for food waste segregation management guide
filepath = './data/nea-fw-segregation-and-treatment-guidebook.pdf'
loader = PyPDFLoader(filepath)
pages = loader.load()

template = """
        Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
        {context}
        Question: {question}
        Helpful Answer:
    """

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)


qa_chain = llm.create_rag_qa_chain(pages, QA_CHAIN_PROMPT)

def process_user_message(user_message):
    return qa_chain.invoke(user_message)['result']