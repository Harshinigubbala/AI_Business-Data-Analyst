# AI-Powered Business Data Analyst

An interactive business analytics dashboard that analyzes the Sample Superstore dataset and answers supported business questions using a rule-based question interpreter.

## Features

- Filter data by region, category, and year.
- View total sales, profit, quantity, and order metrics.
- Explore category, region, state, and monthly sales and profit trends.
- Ask business questions about total sales, profit, and quantity.
- Identify highest-performing and lowest-performing categories, regions, and states.
- Compare business performance across different groups.
- View answers, analysis steps, and supporting results.
- Ask supported follow-up questions.
- Handle ambiguous and unsupported questions with appropriate responses.

## Technology Stack

- Python
- Pandas
- Streamlit
- Plotly
- CSV dataset

## Project Structure

```text
AI_Business_Data_Analyst/
├── data/
│   └── raw/
│       └── Sample - Superstore.csv
├── analysis.py
├── qa_engine.py
├── dashboard.py
├── first_analysis.py
├── validation_report.md
├── architecture.md
├── dfd.md
├── lld.md
└── readme.md
```

## Dataset Description

The project uses the Sample Superstore CSV dataset, which contains fictional retail sales information.

The dataset includes information such as:

- Order ID and customer details.
- Order date and shipping date.
- Product category and sub-category.
- Sales, profit, and quantity.
- Region, state, and city.

**Dataset file:** `data/raw/Sample - Superstore.csv`

**Note:** This is sample retail data and does not represent actual company transactions.

## Data Preparation

The dataset is loaded and processed using Pandas.

The preparation steps include:

1. Loading the CSV dataset into a Pandas DataFrame.
2. Converting order dates into datetime format.
3. Creating year, month, and year-month columns for time-based analysis.
4. Preparing the data for filtering and business calculations.
5. Using the processed DataFrame for dashboard visualizations and question answering.

## Technology Workflow

1. Load the CSV dataset using Pandas.
2. Prepare and process the dataset.
3. Apply region, category, and year filters.
4. Calculate sales, profit, quantity, and other business metrics.
5. Generate charts and tables using Plotly.
6. Process supported business questions using the rule-based question interpreter.
7. Display answers and supporting results in the Streamlit dashboard.

## Setup and Installation

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required packages:

   ```bash
   python -m pip install pandas streamlit plotly
   ```

4. Start the dashboard:

   ```bash
   python -m streamlit run dashboard.py
   ```

5. Open the local URL displayed in the terminal, usually http://localhost:8501.

## Business Analysis

The dashboard supports the following analysis:

- **Sales Analysis:** Understand total sales and compare sales across categories, regions, and states.
- **Profit Analysis:** Identify profitable and loss-making categories, regions, and states.
- **Quantity Analysis:** Examine product quantities and compare performance across groups.
- **Time-Based Analysis:** Explore monthly and yearly business trends.

## Question Answering System

The question-answering component uses a rule-based interpreter implemented in Python.

It supports predefined business questions involving:

- Total sales, profit, and quantity.
- Highest and lowest performance.
- Category-wise analysis.
- Region-wise analysis.
- State-wise analysis.
- Comparison between business groups.
- Supported follow-up questions.

The system uses predefined rules and keywords rather than a generative AI model or an external AI API.

## Validation and Testing

The application was tested using different types of questions and dashboard filters.

Testing includes:

- Total sales, profit, and quantity calculations.
- Highest and lowest performance questions.
- Category, region, and state comparisons.
- Dashboard filter validation.
- Follow-up question handling.
- Ambiguous question handling.
- Unsupported question handling.

Refer to `validation_report.md` for test cases and expected results.

## Limitations

- The question interpreter uses predefined rules and keywords.
- It supports a limited set of measures and groupings.
- It does not understand every natural-language question.
- Results depend on the selected dashboard filters and dataset.
- The dataset contains fictional sample retail information.

## AI Tools

AI tools were used to assist with development, debugging, and documentation. The application itself uses a rule-based question interpreter and does not use a generative AI model or external AI API.

## Risk of Misleading Answers

The dataset is fictional and may not represent actual business performance. Users should interpret the results as sample business analysis rather than real company performance. The dashboard provides analysis steps and supporting results to help users verify answers.

## Future Improvements

- Improve natural-language question understanding.
- Support more business questions and analytical measures.
- Add additional datasets for broader analysis.
- Expand test coverage for different question patterns.
- Improve the question-answering system and dashboard functionality.