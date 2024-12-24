import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import base64




def show_general_data_statistics():
    if "data" in st.session_state:
        data = st.session_state["data"]
        num_var = len(data.columns)
        num_rows = len(data)
        missing_cells = data.isnull().sum().sum()
        missing_cells_percent = (missing_cells / (data.size)) * 100
        duplicate_rows = data.duplicated().sum()
        duplicate_rows_percent = (duplicate_rows / num_rows) * 100
        var_types = data.dtypes.value_counts()

        st.write("### General Data Statistics:")
        st.write(f"- **Number of Variables:**   {num_var}")
        st.write(f"- **Number of Rows:**    {num_rows}")
        st.write(f"- **Missing Cells:**     {missing_cells}")
        st.write(f"- **Missing Cells (%):**     {missing_cells_percent:.2f}%")
        st.write(f"- **Duplicate Rows:**    {duplicate_rows}")
        st.write(f"- **Duplicate Rows (%):**    {duplicate_rows_percent:.2f}%")
        st.write("#### Variable Types:")
        st.write(var_types)
    else:
        st.warning("Please upload a dataset first.")




def describe_data():
    st.title("Describe Data")

    if "data" in st.session_state:
        data = st.session_state["data"]
        st.write("Dataset Description:")
        st.write(data.describe())
    else:
        st.warning("Please upload a dataset first.")


def info_data():
    st.title("Dataset Info")

    if "data" in st.session_state:
        data = st.session_state["data"]
        buffer = io.StringIO()
        data.info(buf=buffer)
        info = buffer.getvalue()
        st.text(info)
    else:
        st.warning("Please upload a dataset first.")

