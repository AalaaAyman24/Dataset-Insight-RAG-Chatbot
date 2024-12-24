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
   cd Dataset-Insight-RAG-Chatbot
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

### After you have run the application, follow these steps to interact with your data and use all the available features:

### 1. *Upload Your Dataset*
- *Upload Data*:  
  - Use the sidebar to upload a CSV or Excel file by clicking the "Upload" button.  
  - The application automatically validates the uploaded file format to ensure it’s ready for processing.

### 2. *Preview Your Data*
- *View and check your data before processing*:  
  - The first few rows of your dataset are displayed to help you verify and inspect the data before making any modifications.

### 3. *Data Cleaning*
- *Ensure correct data types for numeric columns*:  
  - Automatically detects and corrects data types for numeric columns to avoid errors during processing.  
- *Displays unique values for categorical features*:  
  - Helps identify any inconsistencies or anomalies in categorical columns by showing all unique values.

### 4. *Modify Column Names*
- *Easily rename columns for better clarity and consistency*:  
  - Allows you to modify column names to make them more descriptive and easier to understand.

### 5. *General Data Statistics*
- *Get summary statistics like mean, median, and standard deviation for your dataset*:  
  - Quickly assesses the central tendency and distribution of numerical data, helping you understand the overall structure of your dataset.

### 6. *Describe Your Data*
- *Generate detailed descriptive statistics for the dataset*:  
  - Provides metrics such as count, minimum, maximum, and percentiles for each column to help you better understand the distribution and variability of the data.

### 7. *Info About the Dataset*
- *View detailed information about the dataset, such as data types and null values*:  
  - Displays comprehensive information about each column, including its data type and the presence of any missing values. This is useful for cleaning and preprocessing steps.

### 8. *Handle Categorical Columns*
- *The handle_categorical function allows you to handle categorical columns using the following methods*:
  - *One-Hot Encoding*:  
    - Creates binary columns for each category, where each category is represented by a separate column with a 1 or 0 indicating the presence of that category in the row.
  - *Label Encoding*:  
    - Converts categories to numerical values, assigning each category a unique integer, which can be useful for machine learning models that require numeric input.
