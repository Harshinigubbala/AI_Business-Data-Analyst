# Validation Report

## 1. Purpose
This report records tests performed on the AI Business Data Analyst
dashboard using the Sample Superstore dataset.

## 2. Calculation Validation

| Test | Input | Expected Result | Observed Result | Status |
|---|---|---|---|---|
| 1 | What is the total sales? | $2,297,200.86 | $2,297,200.86 | Pass |
| 2 | What is the total profit? | $286,397.02 | $286,397.02 | Pass |
| 3 | What is the total quantity? | 37,873 | 37,873 | Pass |
| 4 | Which category has the highest sales? | Technology — $836,154.03 | Technology — $836,154.03 | Pass |
| 5 | Which state has the lowest profit? | Texas — -$25,729.36 | Texas — -$25,729.36 | Pass |

## 3. Filter Validation

Filters selected: East region and Technology category.

| Metric | Expected Result | Observed Result | Status |
|---|---:|---:|---|
| Total Sales | $264,973.98 | $264,973.98 | Pass |
| Total Profit | $47,462.04 | $47,462.04 | Pass |
| Total Quantity | 1,942 | 1,942 | Pass |

The question-answering results matched the dashboard summary for the
selected filters.

## 4. Follow-up Question Validation

| Initial Question | Follow-up Question | Result |
|---|---|---|
| Which category has the highest sales? | What about profit? | Technology has the highest profit: $145,454.95 |

The system used the previous question's category context to answer
the follow-up.

## 5. Ambiguous and Unsupported Questions

| Input | Expected Behavior | Observed Behavior | Status |
|---|---|---|---|
| Show sales by region | Ask whether the user wants highest, lowest, or comparison | Asked for clarification | Pass |
| What is the weather in Hyderabad? | Explain that the question is unsupported | Returned a message describing supported business questions | Pass |

## 6. Conclusion

The tested calculations matched the expected results. The dashboard
also responded appropriately to the tested follow-up, ambiguous, and
unsupported questions.