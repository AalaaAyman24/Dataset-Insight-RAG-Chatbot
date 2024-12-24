import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import base64


def handle_categorical_values():
    if "data" in st.session_state:
        data = st.session_state["data"]

        st.subheader("Handle Categorical Values")

        categorical_cols_features = list(data.select_dtypes(include="object").columns)

        one_hot_enc = st.multiselect("Select nominal categorical columns", categorical_cols_features)

        if one_hot_enc:
            for column in one_hot_enc:
                if data[column].dtype == 'object':
                    data = pd.get_dummies(data, columns=[column])
            st.session_state["data"] = data
            st.write("### Data after One-Hot Encoding:")
            st.write(data.head())

        label_encoder = LabelEncoder()
        label_enc = st.multiselect("Select ordinal categorical columns", categorical_cols_features)

        if label_enc:
            for column in label_enc:
                if data[column].dtype == 'object':
                    data[column] = label_encoder.fit_transform(data[column])
            st.session_state["data"] = data
            st.write("### Data after Label Encoding:")
            st.write(data.head())

    else:
        st.warning("Please upload a dataset to handle categorical values.")


def handle_missing_values():
    st.title("Handle Missing Values")

    if "data" in st.session_state:
        data = st.session_state["data"].copy()

        action = st.selectbox(
            "Select Action", ["Drop", "Dropna", "Fill missing val"])

        column = st.selectbox("Select Column", data.columns)

        st.write("### Before:")
        st.dataframe(data)

        modified_data = data.copy()

        if action == "Drop":
            modified_data.drop(columns=[column], inplace=True)
        elif action == "Dropna":
            modified_data.dropna(subset=[column], inplace=True)
        elif action == "Fill missing val":
            fill_method = st.selectbox(
                "Select fill method", ["Mean", "Mode", "Median"])

            if fill_method == "Mean":
                fill_value = data[column].mean()
            elif fill_method == "Mode":
                fill_value = data[column].mode()[0]
            elif fill_method == "Median":
                fill_value = data[column].median()

            modified_data[column].fillna(fill_value, inplace=True)

        st.write("### After (Preview):")
        st.dataframe(modified_data)

        if st.button("OK"):
            st.session_state["data"] = modified_data
            st.success("Done! The action has been applied.")
            st.write("### After:")
            st.dataframe(modified_data)

    else:
        st.warning("Please upload a dataset first.")

def handle_duplicates():
    st.title("Handle Duplicates")

    if "data" in st.session_state:
        data = st.session_state["data"].copy()

        action = st.selectbox(
            "Select Action", ["Drop Duplicates", "Drop Duplicates in Column", "Keep First", "Keep Last"])

        if action in ["Drop Duplicates in Column", "Keep First", "Keep Last"]:
            column = st.selectbox("Select Column", data.columns)
        else:
            column = None

        st.write("### Before:")
        st.dataframe(data)

        modified_data = data.copy()

        if action == "Drop Duplicates":
            modified_data.drop_duplicates(inplace=True)
        elif action == "Drop Duplicates in Column":
            modified_data.drop_duplicates(subset=[column], inplace=True)
        elif action == "Keep First":
            modified_data.drop_duplicates(
                subset=[column], keep="first", inplace=True)
        elif action == "Keep Last":
            modified_data.drop_duplicates(
                subset=[column], keep="last", inplace=True)

        st.write("### After (Preview):")
        st.dataframe(modified_data)

        if st.button("OK"):
            st.session_state["data"] = modified_data
            st.success("Done! The action has been applied.")
            st.write("### After:")
            st.dataframe(modified_data)

    else:
        st.warning("Please upload a dataset first.")


def handle_outliers():
    st.title("Handle Outliers")

    if "data" in st.session_state:
        data = st.session_state["data"].copy()

        column = st.selectbox("Select Column", data.select_dtypes(
            include=[np.number]).columns)

        action = st.selectbox(
            "Select Action",
            ["Remove Outliers (IQR)", "Set Bounds Manually",
             "Replace Outliers"]
        )

        st.write("### Before:")
        st.dataframe(data)

        modified_data = data.copy()

        if action == "Remove Outliers (IQR)":
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Remove outliers
            modified_data = modified_data[(
                modified_data[column] >= lower_bound) & (modified_data[column] <= upper_bound)]

        elif action == "Set Bounds Manually":
            # User inputs for bounds
            lower_bound = st.number_input(
                f"Set lower bound for {column}", value=float(data[column].min()))
            upper_bound = st.number_input(
                f"Set upper bound for {column}", value=float(data[column].max()))

            modified_data = modified_data[(
                modified_data[column] >= lower_bound) & (modified_data[column] <= upper_bound)]

        elif action == "Replace Outliers":

            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            replace_method = st.radio(
                "Select Replacement Method",
                ["Mean", "Median"]
            )

            if replace_method == "Mean":
                replacement_value = data[column].mean()
            else:
                replacement_value = data[column].median()

            # Replace outliers
            modified_data[column] = modified_data[column].apply(
                lambda x: replacement_value if x < lower_bound or x > upper_bound else x
            )

        # After Visualization
        st.write("### After (Preview):")
        st.dataframe(modified_data)

        if st.button("OK"):
            st.session_state["data"] = modified_data
            st.success("Done! The action has been applied.")
            st.write("### After:")
            st.dataframe(modified_data)

    else:
        st.warning("Please upload a dataset first.")
