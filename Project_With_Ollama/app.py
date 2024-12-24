from langchain_text_splitters import RecursiveCharacterTextSplitter
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
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from sentence_transformers import SentenceTransformer, util
from langchain.schema import Document
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.chains import create_history_aware_retriever
from langchain_huggingface import HuggingFaceEmbeddings
# from RAG import create_doucment, ask_me, load_models_embedding, load_models_llm, create_database
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
        background-color: #B22222;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 5px;
    }
    .small-button:hover {
        background-color: #B22222;
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


def prepare_and_split_docs(file):
    split_docs = []

    text = file.to_string(index=False)

    document = Document(page_content=text)

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=512,
        chunk_overlap=256,
        disallowed_special=(),
        separators=["\n\n", "\n", " "]
    )

    split_docs.extend(splitter.split_documents([document]))

    return split_docs


def ingest_into_vectordb(split_docs):
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.from_documents(split_docs, embeddings)
    DB_FAISS_PATH = 'vectorstore/db_faiss'
    db.save_local(DB_FAISS_PATH)
    return db


def get_conversation_chain(retriever):
    llm = Ollama(model="llama3.2:1b")
    contextualize_q_system_prompt = (
        "Given the chat history and the latest user question, "
        "provide a response that directly addresses the user's query based on the provided documents. "
        "Do not rephrase the question or ask follow-up questions."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    system_prompt = (
        "As a personal chat assistant, provide accurate and relevant information based on the provided document. "
        "Ensure that the answer is clear, concise, and directly addresses the question without extra details."
        "{context}"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(
        history_aware_retriever, question_answer_chain)

    store = {}

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    return conversational_rag_chain


def calculate_similarity_score(answer: str, context_docs: list) -> float:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    context_docs = [doc.page_content for doc in context_docs]
    answer_embedding = model.encode(answer, convert_to_tensor=True)
    context_embeddings = model.encode(context_docs, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(answer_embedding, context_embeddings)
    max_score = similarities.max().item()
    return max_score


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


# api = "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21"


def rag_chatbot():
    st.title("RAG Chatbot⁉️")
    st.markdown(button_style, unsafe_allow_html=True)

    # Check if data is uploaded and available
    if "data" in st.session_state and isinstance(st.session_state["data"], pd.DataFrame):
        df = st.session_state["data"]

        # Prepare documents from the dataset
        with st.spinner("Preparing documents..."):
            split_docs = prepare_and_split_docs(df)
            vector_store = ingest_into_vectordb(split_docs)
            retriever = vector_store.as_retriever()

        # Initialize the conversation chain
        conversational_chain = get_conversation_chain(retriever)
        st.session_state.conversational_chain = conversational_chain

        # Initialize the conversational RAG chain
        conversational_chain = get_conversation_chain(retriever)

        # Chat Interface
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        # Chat input
        st.markdown(button_style, unsafe_allow_html=True)
        user_input = st.text_input("Ask a question about the dataset:",
                                   key="user_input", placeholder="Type your question here...")

        if st.button("Send"):
            st.markdown(button_style, unsafe_allow_html=True)
            if user_input and 'conversational_chain' in st.session_state:
                session_id = "abc123"
                conversational_chain = st.session_state.conversational_chain
                response = conversational_chain.invoke({"input": user_input}, config={
                    "configurable": {"session_id": session_id}})
                context_docs = response.get('context', [])
                st.session_state.chat_history.append(
                    {"user": user_input, "bot": response['answer'], "context_docs": context_docs})

        # Display chat history
        if st.session_state.chat_history:
            for message in st.session_state.chat_history:
                st.markdown(user_template.format(
                    msg=message['user']), unsafe_allow_html=True)
                st.markdown(bot_template.format(
                    msg=message['bot']), unsafe_allow_html=True)

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
