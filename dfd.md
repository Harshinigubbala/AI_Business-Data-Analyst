# Data Flow Diagram (DFD)

## Level 0: Context Diagram

```text
        User
          |
          | Selects filters / asks a question
          v
+--------------------------------+
| AI Business Data Analyst       |
|          Dashboard             |
+--------------------------------+
          |
          | Displays metrics, charts,
          | tables, and answers
          v
        User
```

## Level 1: Detailed Data Flow

```text
+--------------------+
| Sample Superstore  |
| CSV Dataset        |
+--------------------+
          |
          v
+--------------------+
| 1. Load and Prepare|
| Data (analysis.py) |
+--------------------+
          |
          v
+--------------------+       +--------------------+
| 2. Apply Dashboard |<------| User Selects       |
| Filters            |       | Region/Category/Year|
+--------------------+       +--------------------+
          |
          +--------------------------+
          |                          |
          v                          v
+--------------------+     +--------------------+
| 3. Calculate       |     | 4. Process User    |
| Metrics and Charts |     | Question (qa_engine)|
+--------------------+     +--------------------+
          |                          |
          +-------------+------------+
                        |
                        v
              +--------------------+
              | 5. Display Results |
              | Dashboard / Answer |
              +--------------------+
                        |
                        v
                      User
```

## Explanation

1. The dataset is loaded from the CSV file.
2. The user selects region, category, and year filters.
3. The dashboard applies the selected filters to the data.
4. The system calculates metrics and creates charts.
5. The question-answering engine processes supported questions using the filtered data.
6. The dashboard displays the results to the user.