import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import base64
import json
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from Information import *
from Preprocessing1 import *
from Preprocessing2 import *
from Virtualization import *


bot_template = '''
<div style="display: flex; align-items: center; margin-bottom: 10px; background-color: #B22222; padding: 10px; border-radius: 10px; border: 1px solid #7A0000;">
    <div style="flex-shrink: 0; margin-right: 10px;">
        <img src="https://raw.githubusercontent.com/AalaaAyman24/Test/main/chatbot.png" 
             style="max-height: 50px; max-width: 50px; object-fit: cover;">
    </div>
    <div style="background-color: #B22222; color: white; padding: 10px; border-radius: 10px; max-width: 75%; word-wrap: break-word; overflow-wrap: break-word;">
        {msg}
    </div>
</div>
'''


user_template = '''
<div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: flex-end;">
    <div style="flex-shrink: 0; margin-left: 10px;">
        <img src="https://raw.githubusercontent.com/AalaaAyman24/Test/main/question.png"
             style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div style="background-color: #757882; color: white; padding: 10px; border-radius: 10px; max-width: 75%; word-wrap: break-word; overflow-wrap: break-word;">
        {msg}
    </div>
</div>
'''

button_style = """
<style>
    .small-button {
        display: inline-block;
        padding: 5px 10px;
        font-size: 12px;
        color: white;
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 5px;
    }
    .small-button:hover {
        background-color: #0056b3;
    }
    .chat-box {
        position: fixed;
        bottom: 20px;
        width: 100%;
        left: 0;
        padding: 20px;
        background-color: #f1f1f1;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
"""


def create_documents(df):
    """Converts a DataFrame into a list of Document objects."""
    documents = [
        Document(
            metadata={"id": str(i)},
            page_content=json.dumps(row.to_dict())
        )
        for i, row in df.iterrows()
    ]
    return documents


def load_embedding_model():
    """Loads the embedding model for vectorization."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def load_llm(api_key):
    """Loads the LLM model for answering queries."""
    return HuggingFaceHub(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        huggingfacehub_api_token=api_key,
        model_kwargs={"temperature": 0.5, "max_length": 100}
    )


def ask_question(question, retriever, llm):
    """Uses a QA chain to retrieve and answer a question."""
    qa_chain = RetrievalQA.from_chain_type(
        retriever=retriever,
        chain_type="stuff",
        llm=llm,
        return_source_documents=False
    )
    response = qa_chain.invoke({"query": question})
    return response["result"]

# Streamlit App


def upload_data():
    st.title("Upload Dataset")
    file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

    if file:
        try:
            if file.name.endswith(".csv"):
                data = pd.read_csv(file)
            elif file.name.endswith(".xlsx"):
                data = pd.read_excel(file)

            st.session_state["data"] = data
            st.success("Dataset uploaded successfully!")
        except Exception as e:
            st.error(f"Error loading file: {e}")


def download_data():
    """Downloads the DataFrame as a CSV file."""
    if "data" in st.session_state and not st.session_state["data"].empty:
        csv = st.session_state["data"].to_csv(index=False).encode('utf-8')

        download_button = st.download_button(
            label="Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

        if download_button:
            st.balloons()
            st.success("Dataset is ready for download!")

    else:
        st.warning(
            "No data available to download. Please modify or upload a dataset first.")


api = "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21"


def rag_chatbot():
    st.title("RAG Chatbot")
    st.markdown(button_style, unsafe_allow_html=True)

    # Check if data is uploaded and available
    if "data" in st.session_state and isinstance(st.session_state["data"], pd.DataFrame):
        df = st.session_state["data"]

        # Convert data to documents
        documents = create_documents(df)

        # Load models
        embedding_model = load_embedding_model()
        llm_model = load_llm(api_key=api[:-2])
        retriever = FAISS.from_documents(
            documents, embedding=embedding_model).as_retriever()

        # Chat Interface
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        question = st.text_area(
            "Ask a question about your dataset:", key="question_input")
        if st.button("Send", key="send_button"):
            if question.strip():
                # Append user message
                st.session_state["chat_history"].append(
                    {"role": "user", "content": question})

                # Generate response
                response = ask_question(question, retriever, llm_model)
                st.session_state["chat_history"].append(
                    {"role": "bot", "content": response})

        # Render chat history
        for message in st.session_state["chat_history"]:
            if message["role"] == "user":
                st.markdown(user_template.format(
                    msg=message["content"]), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.format(
                    msg=message["content"]), unsafe_allow_html=True)
    else:
        st.warning("Please upload a dataset to proceed.")


def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio(
        "Go to",
        [
            "Upload",
            "Preview",
            "Data Cleaning",
            "Modify Column Names",
            "General Data Statistics",
            "Describe",
            "Info",
            "Handle Categorical",
            "Missing Values",
            "Handle Duplicates",
            "Handle Outliers",
            "Visualize Data",
            "Download",
            "RAG Chatbot"
        ],
        key="unique_navigation_key",
    )

    if options == "Upload":
        upload_data()
    elif options == "Preview":
        preview_data()
    elif options == "Data Cleaning":
        data_cleaning()
    elif options == "Modify Column Names":
        modify_column_names()
    elif options == "General Data Statistics":
        show_general_data_statistics()
    elif options == "Describe":
        describe_data()
    elif options == "Info":
        info_data()
    elif options == "Handle Categorical":
        handle_categorical_values()
    elif options == "Missing Values":
        handle_missing_values()
    elif options == "Handle Duplicates":
        handle_duplicates()
    elif options == "Handle Outliers":
        handle_outliers()
    elif options == "Visualize Data":
        visualize_data()
    elif options == "Download":
        download_data()
    elif options == "RAG Chatbot":
        rag_chatbot()

    else:
        st.warning("Please upload a dataset first.")


if __name__ == "__main__":
    main()
