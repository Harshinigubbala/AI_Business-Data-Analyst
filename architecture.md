# System Architecture

## Overview
The AI Business Data Analyst is a Python-based dashboard that loads
business data, applies user-selected filters, analyzes the data, and
answers natural-language business questions.

## Architecture Diagram

```text
                  User
                   |
                   v
          Streamlit Dashboard
             (dashboard.py)
                   |
          +--------+--------+
          |                 |
          v                 v
    Dashboard Views    Question Input
          |                 |
          v                 v
    analysis.py        qa_engine.py
          |                 |
          +--------+--------+
                   |
                   v
          Pandas DataFrame
                   |
                   v
       Sample Superstore CSV