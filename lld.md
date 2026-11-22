# Low-Level Design (LLD)

## 1. Project Overview
The AI Business Data Analyst uses Python, Pandas, Streamlit, and Plotly
to analyze the Sample Superstore dataset and answer supported business
questions.

## 2. Modules

### A. analysis.py
**Purpose:** Load and analyze the dataset.

- `load_data()`: Reads the CSV file and prepares date-related columns.
- `get_business_summary(df)`: Calculates total sales, profit, quantity,
  and unique orders.
- `get_category_analysis(df)`: Summarizes results by category.
- `get_region_analysis(df)`: Summarizes results by region.
- `get_state_analysis(df)`: Summarizes results by state.
- `get_monthly_analysis(df)`: Summarizes sales and profit by month.

**Input:** Dataset as a Pandas DataFrame, where applicable.  
**Output:** Prepared data and analysis results.

### B. qa_engine.py
**Purpose:** Interpret supported business questions and calculate answers.

- Identifies supported measures: sales, profit, and quantity.
- Identifies supported groupings: category, region, and state.
- Handles highest, lowest, total, comparison, and supported follow-up
  questions.
- Returns an answer, analysis steps, and supporting data.
- Requests clarification for ambiguous questions and reports unsupported
  questions.

**Input:** Filtered DataFrame, user question, and previous question context.  
**Output:** Answer text, analysis steps, and supporting results.

### C. dashboard.py
**Purpose:** Provide the interactive user interface.

- Loads the dataset and displays dashboard filters.
- Applies region, category, and year filters.
- Displays summary metrics, charts, and a data table.
- Accepts user questions and displays the QA engine's response.
- Maintains limited context for follow-up questions during the session.

**Input:** User selections and questions.  
**Output:** Interactive dashboard and analysis results.

## 3. Data Processing Flow

1. Read the CSV dataset.
2. Prepare date columns and derive year/month fields.
3. Apply the user's selected dashboard filters.
4. Calculate summary metrics and grouped analyses.
5. Pass the filtered data and question to the QA engine.
6. Display the answer, analysis steps, and supporting results.

## 4. Error and Limitation Handling

- Empty questions prompt the user to enter a question.
- Ambiguous supported questions request clarification.
- Unsupported questions receive a message listing the supported topics.
- The question interpreter uses predefined rules and keywords; it is not
  a general-purpose AI language model.
- Answers are limited to the dataset, supported measures, and supported
  groupings.

## 5. Technology Stack

- Python: application logic
- Pandas: data loading and analysis
- Streamlit: dashboard interface
- Plotly: interactive charts
- CSV: dataset storage