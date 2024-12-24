import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def visualize_data():
    st.title("Data Visualization")

    if "data" in st.session_state:
        df = st.session_state["data"]

        chart_type = st.selectbox("Choose Chart Type", [
                                  "Bar Chart", "Histogram", "Boxplot", "Doughnut Chart", "Pie Chart"])

        columns = df.select_dtypes(include=['number']).columns.tolist()
        selected_column = st.selectbox("Select Column", columns)

        value_counts = df[selected_column].value_counts()

        if chart_type == "Bar Chart":
            if len(value_counts) > 20:
                st.warning(
                    "Bar Chart is not suitable for more than 20 unique values. Please select a column with 20 or fewer unique values.")
            else:
                st.subheader(f"Bar Chart for {selected_column}")
                fig, ax = plt.subplots()
                df[selected_column].value_counts().plot(kind='bar', ax=ax)
                st.pyplot(fig)

        elif chart_type == "Histogram":
            if len(value_counts) < 10:
                st.warning(
                    "Histogram requires at least 10 unique values to be meaningful. Please select a column with more than 10 unique values.")
            else:
                st.subheader(f"Histogram for {selected_column}")
                fig, ax = plt.subplots()
                ax.hist(df[selected_column], bins=20, edgecolor="black")
                ax.set_xlabel(selected_column)
                ax.set_ylabel('Frequency')
                st.pyplot(fig)

        elif chart_type == "Boxplot":
            if len(value_counts) < 5:
                st.warning(
                    "Boxplot requires at least 5 unique values to show distribution. Please select a column with more than 5 unique values.")
            else:
                st.subheader(f"Boxplot for {selected_column}")
                fig = plt.figure(figsize=(6, 4))
                sns.boxplot(x=df[selected_column])
                st.pyplot(fig)

        elif chart_type == "Doughnut Chart":
            if len(value_counts) > 5:
                st.warning(
                    "Doughnut Chart is not suitable for more than 5 unique values. Please select a column with 5 or fewer unique values.")
            else:
                st.subheader(f"Doughnut Chart for {selected_column}")
                fig = px.pie(value_counts, names=value_counts.index,
                             values=value_counts.values, hole=0.3)
                st.plotly_chart(fig)

        elif chart_type == "Pie Chart":
            if len(value_counts) > 5:
                st.warning(
                    "Pie Chart is not suitable for more than 5 unique values. Please select a column with 5 or fewer unique values.")
            else:
                st.subheader(f"Pie Chart for {selected_column}")
                fig = px.pie(value_counts, names=value_counts.index,
                             values=value_counts.values)
                st.plotly_chart(fig)

    else:
        st.warning("Please upload a dataset first.")
