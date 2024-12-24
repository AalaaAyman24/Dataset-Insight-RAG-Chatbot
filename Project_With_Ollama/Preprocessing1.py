import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import base64


def preview_data():
    if "data" in st.session_state:
        data = st.session_state["data"]

        st.write("### Dataset Preview Options:")

        preview_option = st.radio(
            "Select how to preview the dataset:",
            options=["Head", "Tail", "Custom Number of Rows"],
            index=0
        )

        if preview_option == "Head":
            st.write("### First 5 Rows of the Dataset:")
            st.dataframe(data.head())
        elif preview_option == "Tail":
            st.write("### Last 5 Rows of the Dataset:")
            st.dataframe(data.tail())
        elif preview_option == "Custom Number of Rows":
            number = st.slider(
                "Select Number of Rows to Display:", 1, len(data))
            st.write(f"### First {number} Rows of the Dataset:")
            st.dataframe(data.head(number))

        if st.checkbox("Show all data"):
            st.write(data)

        if st.checkbox("Show Column Names"):
            st.write(data.columns)

        if st.checkbox("Show Dimensions"):
            st.write(data.shape)

    else:
        st.warning("Please upload a dataset to view options.")


def data_cleaning():
    if "data" in st.session_state:
        data = st.session_state["data"]

        st.subheader("Data Cleaning")

        col_option = st.selectbox("Choose your option", [
            "Check all numeric features are numeric?", "Show unique values of categorical features"])

        if col_option == "Check all numeric features are numeric?":
            st.write("Converting all numeric columns to numeric types...")
            numeric_columns = list(
                data.select_dtypes(include=np.number).columns)
            if numeric_columns:
                for col in numeric_columns:
                    data[col] = pd.to_numeric(data[col], errors='coerce')

                st.session_state["data"] = data
                st.success("Done!")
            else:
                st.info(
                    "All features are already numeric or there are no numeric features in the dataset.")

        elif col_option == "Show unique values of categorical features":
            st.write("Unique values for categorical features:")
            for column in data.columns:
                if data[column].dtype == object:
                    st.write(f"{column}: {data[column].unique()}")
            else:
                st.info("No categorical features detected in the dataset.")
    else:
        st.warning("Please upload a dataset to perform data cleaning.")


def modify_column_names():
    st.title("Modify Column Names")

    if "data" in st.session_state:
        df = st.session_state["data"]

        if "modified_columns" not in st.session_state:
            st.session_state.modified_columns = list(df.columns)

        st.write('### *Current Column Names*')
        st.table(df.columns)

        st.write('### *Modify Column Names*')
        with st.expander("Modify Column Names", expanded=True):
            before_col = st.session_state.modified_columns
            before_col_df = pd.DataFrame(before_col, columns=['Column Name'])
            st.table(before_col_df)

            col3, col4, col5, col6 = st.columns(4)
            changes_made = False

            if st.button('Convert to Uppercase'):
                st.session_state.modified_columns = [
                    col.upper() for col in before_col]
                changes_made = True
            if st.button('Convert to Lowercase'):
                st.session_state.modified_columns = [
                    col.lower() for col in before_col]
                changes_made = True
            if st.button('Replace Spaces with Underscore'):
                st.session_state.modified_columns = [
                    col.replace(" ", "_") for col in before_col]
                changes_made = True
            if st.button('Capitalize First Letters'):
                st.session_state.modified_columns = [
                    col.title() for col in before_col]
                changes_made = True

            if changes_made:
                df.columns = st.session_state.modified_columns
                st.session_state["data"] = df
                st.success("Changes applied successfully.")
                st.table(pd.DataFrame(
                    df.columns, columns=['Modified Columns']))

        st.write("### *Modify a Specific Column Name*")
        column_select = st.selectbox(
            'Select column to modify', options=st.session_state.modified_columns)
        new_column_name = st.text_input('Enter new column name')
        if st.button('Update Column Name'):
            if column_select and new_column_name:
                st.session_state.modified_columns = [
                    new_column_name if col == column_select else col for col in st.session_state.modified_columns]
                df.columns = st.session_state.modified_columns
                st.session_state["data"] = df
                st.success("Column name updated.")
                st.table(pd.DataFrame(
                    df.columns, columns=['Modified Columns']))

    else:
        st.warning("Please upload a dataset first.")
