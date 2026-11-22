# AI-Powered Business Data Analyst

An interactive dashboard that analyzes the Sample Superstore dataset
and answers supported business questions using a rule-based question
interpreter.

## Features

- Filter data by region, category, and year.
- View sales, profit, quantity, and order metrics.
- Explore category, region, state, and monthly trends.
- Ask supported questions about total sales, profit, quantity, and
  performance by category, region, or state.
- View answers, analysis steps, and supporting results.
- Ask supported follow-up questions.

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
└── README.md
```

## Setup

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

5. Open the local URL displayed in the terminal, usually
   `http://localhost:8501`.

## Dataset

The project uses the Sample Superstore CSV dataset. It is fictional
sample retail data and does not represent actual company sales.

## Validation

Refer to `validation_report.md` for calculation, filter, follow-up,
ambiguous-question, and unsupported-question tests.

## Limitations

- The question interpreter uses predefined rules and keywords.
- It supports a limited set of measures and groupings.
- It does not understand every natural-language question.
- Results depend on the selected dashboard filters and the dataset.

## AI Tools

The question-answering component is a rule-based interpreter. It does
not use a generative AI model or an external AI API.
