---

# Dataset-Insight-RAG-Chatbot

Welcome to the *Streamlit Dataset Processing and Retrieval Augmented Generation (RAG) Chatbot* project! This application provides a powerful and user-friendly interface for preprocessing datasets, visualizing data, and interacting with a chatbot to answer queries about your dataset.

---

## Features  

- **Upload**: Upload data from CSV and Excel files with automatic validation.  
- **Preview**: View and inspect your data before processing.  
- **Data Cleaning**: Clean your data by ensuring correct data types for numeric columns and displaying unique values for categorical features. 
- **Modify Column Names**: Easily rename columns for better clarity and consistency.  
- **General Data Statistics**: Get summary statistics like mean, median, and standard deviation for your dataset.  
- **Describe**: Generate descriptive statistics to understand your dataset better.  
- **Info**: View detailed information about the dataset, such as data types and null values.  
- **Handle Categorical**: Process categorical data using One-Hot Encoding or Label Encoding.  
- **Missing Values**: Handle and fill missing values using various strategies.  
- **Handle Duplicates**: Detect and remove duplicate entries.  
- **Handle Outliers**: Identify and manage outliers for more accurate analysis.  
- **Visualize Data**: Generate various charts and visualizations to explore the data.  
- **Modeling**: Apply machine learning models and predictive analysis to your data.  
- **Download**: Download the processed data in your preferred format.  
- **RAG Chatbot**: Interact with the chatbot powered by an API or Ollama for data assistance and queries.

---

## Installation

To set up the Streamlit Dataset Processing and Retrieval Augmented Generation (RAG) Chatbot project on your local machine, follow the steps below:

### Prerequisites:
Make sure you have Python 3.6+ installed on your system.

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AalaaAyman24/Dataset-Insight-RAG-Chatbot.git
   cd streamlit-dataset-processing-rag-chatbot
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Once the application is installed, you can run it using the following command:

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501` to start using the application.

---
