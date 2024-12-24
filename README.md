---

# Dataset-Insight-RAG-Chatbot 📊🤖

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
    - Creates binary columns for each category, where each category is represented by a separate column with a `1` or `0` indicating the presence of that category in the row.
  - *Label Encoding*:  
    - Converts categories to numerical values, assigning each category a unique integer, which can be useful for machine learning models that require numeric input.

### 9. *Handle Missing Values* 
The `handle_missing_values` function provides several methods to handle missing values in your dataset. You can choose from the following options:

- **Drop**:  
  Removes rows containing any missing values.

- **Dropna**:  
  Removes rows that specifically have null or missing entries.

- **Fill Missing Values**:  
  Allows you to fill missing values with one of the following options:
  - **Mean**: Fills missing values with the mean value of the respective column.
  - **Mode**: Fills missing values with the mode (most frequent value) of the column.
  - **Median**: Fills missing values with the median value of the respective column.

> **After Preview**: The preview shows how the dataset will look after handling missing values (either by dropping rows or filling them). You can inspect the changes before confirming. Once you're happy with the preview, click "OK" to apply the action.


### 10. *Handle Duplicates*  
The `handle_duplicates` function provides methods to manage duplicate rows in your dataset. You can choose one of the following options:

- **Drop Duplicates in Column**:  
  Removes duplicate rows based on specific columns you select. This ensures no two rows have identical values in the chosen columns.

- **Keep First**:  
  Keeps the first occurrence of each duplicate set and removes the subsequent duplicates.

- **Keep Last**:  
  Keeps the last occurrence of each duplicate set and removes the others.

> **After Preview**: A preview of the dataset is displayed, showing the effect of removing or keeping duplicates. You can review the changes before applying them. Once you're satisfied with the preview, click "OK" to apply the changes to your data.


### 11. *Handle Outliers* 
The `handle_outliers` function provides methods to identify and manage outliers in numerical columns. The following options are available:

- **Remove Outliers (IQR)**:  
  Removes outliers based on the Interquartile Range (IQR). Outliers are values that lie outside this range and are removed to ensure the data remains within a reasonable range.

- **Set Bounds Manually**:  
  Allows you to manually set the upper and lower bounds for your data, removing values that fall outside the specified range.

- **Replace Outliers**:  
  Replaces outliers with a predefined value, such as the mean or median of the column, reducing their impact on the dataset.

> **After Preview**: Preview the effect of handling outliers on your dataset. You can review how removing or replacing outliers will affect your data. Once satisfied, click "OK" to apply the changes.


### 12. *Data Visualization*

The `visualize_data()` function provides a simple way to visualize various aspects of your dataset through different types of charts. It allows you to interactively select chart types and columns, making it easy to explore your data visually.

Here’s a breakdown of how the function works:

1. **Chart Type Selection**  
   The user is prompted to select the type of chart they would like to visualize. Available chart options include:
   - **Bar Chart**
   - **Histogram**
   - **Boxplot**
   - **Doughnut Chart**
   - **Pie Chart**

2. **Column Selection**  
   After selecting the chart type, the user is asked to choose a numerical column from the dataset to visualize. The available columns are automatically filtered to only include numerical columns.

3. **Generating and Displaying Charts**  
   Based on the selected chart type and column, the function generates the respective chart and displays it. Here’s how each chart type is handled:

   - **Bar Chart**  
     A bar chart is suitable for visualizing the frequency of categorical data or counts of unique values in a column. However, it’s not recommended if the column has more than 20 unique values, as the chart can become cluttered. If the selected column has fewer than 20 unique values, a bar chart is generated, showing the frequency of each category.

   - **Histogram**  
     A histogram is used to display the distribution of numerical data. It is especially useful for understanding the spread and frequency of values in a dataset. Histograms require at least 10 unique values to be meaningful, and if the selected column meets this condition, a histogram is generated.

   - **Boxplot**  
     A boxplot visualizes the distribution of data through quartiles, showing the median, upper, and lower quartiles, as well as any outliers. A boxplot requires at least 5 unique values to show a proper distribution. If this condition is met, a boxplot is generated.

   - **Doughnut Chart**  
     A doughnut chart is similar to a pie chart but with a hole in the center, giving it a donut-like appearance. This chart is useful for visualizing proportions of categorical data but is recommended only when the column has fewer than 5 unique values.

   - **Pie Chart**  
     Like the doughnut chart, a pie chart shows the proportion of different categories in a dataset. It is most effective with fewer than 5 unique values to avoid overcrowding the chart.

4. **Warnings and User Feedback**  
   If the user selects a column with too many unique values for a particular chart type (e.g., more than 20 unique values for a bar chart), the function will display a warning. This ensures that the user can make informed decisions about which visualization type to use.


### 13. *Download Processed Data*
- **Download Data**: 
  - Once you’ve processed and cleaned your data, you can download it in your preferred format (CSV or Excel) by clicking the "Download Processed Data" button in the sidebar.
  - This allows you to use the cleaned and transformed data for further analysis or to share it with others.

### 14. *RAG Chatbot Integration*

The **RAG (Retrieval Augmented Generation) Chatbot** is integrated into this application to provide an interactive way to ask questions about your dataset. You can use the chatbot to get instant answers and insights about your data without needing to manually analyze it. The chatbot uses advanced language models to generate relevant responses based on your queries.

There are **two options** available for using the RAG Chatbot:

1. **RAG Model with Ollama (Llama 3.2:1b)**:
   - This option utilizes the Ollama API, which is powered by the **Llama 3.2:1b** model. It is designed to offer high-performance responses and assist with data-related queries.
   
2. **RAG API from Hugging Face**:
   - The second option is a free, open-access **API from Hugging Face**. This API is always available, and you get **1000 free requests** to use every month. The Hugging Face API provides another reliable way to integrate the RAG functionality, ensuring that you can still get quick insights into your dataset with minimal setup.

Both options provide the same core functionality but offer different performance levels and access restrictions. You can choose the one that best suits your needs based on available requests and performance preferences.

To use the RAG Chatbot, simply type your query into the chatbot interface and get immediate insights about your dataset. Whether you're interested in data patterns, statistics, or need specific information, the RAG model will respond with helpful answers based on the information it has from the dataset.

---

## Conclusion
The Streamlit Dataset Processing and Retrieval Augmented Generation (RAG) Chatbot application offers a comprehensive solution for efficient dataset preprocessing, data visualization, and seamless interaction with a smart chatbot. By leveraging powerful data-cleaning, transformation, and visualization tools, users can quickly gain valuable insights into their data. The intuitive interface and advanced features, including RAG chatbot integration for automated queries, allow both novice and experienced data analysts to perform in-depth analysis with ease. Whether you're cleaning data, visualizing trends, or asking specific dataset-related questions, this application simplifies the entire process, helping you to make data-driven decisions efficiently.

---

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Pandas & NumPy**: 
- Integration with additional machine learning models for advanced analytics.
- Support for more file formats, such as JSON and Parquet.
- Improved chatbot responses using domain-specific models.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## Contact

For any inquiries or feedback, please contact:
**Aalaa Ayman**
- Email: [aalaasalah389@gmail.com]
- GitHub: [https://github.com/AalaaAyman24]

---

Thank you for using the **Streamlit Dataset Processing and RAG Chatbot** application!🙌🏻

---

