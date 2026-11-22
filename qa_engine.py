
import pandas as pd


def answer_question(df, question, previous_question=None):

    question = question.lower().strip()

    previous_question = (
        previous_question.lower().strip()
        if previous_question else ""
    )

    # STEP 1: Identify the measure
    if any(word in question for word in ["profit", "loss"]):
        measure = "Profit"

    elif any(word in question for word in ["quantity", "units"]):
        measure = "Quantity"

    elif any(word in question for word in ["sales", "revenue"]):
        measure = "Sales"

    elif "profit" in previous_question:
        measure = "Profit"

    elif "quantity" in previous_question:
        measure = "Quantity"

    elif "sales" in previous_question:
        measure = "Sales"

    else:
        measure = None

    # STEP 2: Identify the grouping column
    if "category" in question:
        group_column = "Category"

    elif "region" in question:
        group_column = "Region"

    elif "state" in question:
        group_column = "State"

    elif "category" in previous_question:
        group_column = "Category"

    elif "region" in previous_question:
        group_column = "Region"

    elif "state" in previous_question:
        group_column = "State"

    else:
        group_column = None

    # STEP 3: Identify the requested analysis
    highest = any(
        word in question
        for word in ["highest", "maximum", "top", "most"]
    )

    lowest = any(
        word in question
        for word in ["lowest", "minimum", "least"]
    )

    if not highest and not lowest:
        highest = any(
            word in previous_question
            for word in ["highest", "maximum", "top", "most"]
        )

        lowest = any(
            word in previous_question
            for word in ["lowest", "minimum", "least"]
        )

    compare = any(
        word in question
        for word in ["compare", "comparison"]
    )

    # STEP 4: Handle unsupported questions
    supported_words = [
        "sales", "revenue", "profit", "loss",
        "quantity", "units",
        "category", "region", "state",
        "total", "overall", "sum",
        "highest", "maximum", "top", "most",
        "lowest", "minimum", "least",
        "compare", "comparison"
    ]

    if not any(word in question for word in supported_words):
        return {
            "answer": "Sorry, I couldn't understand this question. Please ask about total sales, profit, quantity, or performance by category, region, or state.",
            "steps": "The question does not match a supported business analysis.",
            "data": None
        }

    # STEP 5: Handle unclear measures
    if measure is None:
        return {
            "answer": "Please specify the measure: Sales, Profit, or Quantity.",
            "steps": "The question does not clearly identify which business measure to analyse.",
            "data": None
        }

    # STEP 6: Handle grouped analysis
    if group_column:

        if highest and lowest:
            return {
                "answer": "Your question asks for both highest and lowest results. Please ask for one at a time.",
                "steps": "The requested ranking is ambiguous.",
                "data": None
            }

        result = df.groupby(group_column)[measure].sum().reset_index()

        if highest:
            result = result.sort_values(
                by=measure, ascending=False
            )
            selected = result.iloc[0]
            direction = "highest"

        elif lowest:
            result = result.sort_values(
                by=measure, ascending=True
            )
            selected = result.iloc[0]
            direction = "lowest"

        elif compare:
            result = result.sort_values(
                by=measure, ascending=False
            )

            return {
                "answer": f"Here is the comparison of {measure.lower()} by {group_column.lower()}.",
                "steps": f"Grouped records by {group_column} and calculated total {measure.lower()} for each group.",
                "data": result
            }

        else:
            return {
                "answer": f"Would you like the highest, lowest, or a comparison of {measure.lower()} by {group_column.lower()}?",
                "steps": "The question identifies a measure and grouping but does not specify the analysis.",
                "data": None
            }

        return {
            "answer": f"{selected[group_column]} has the {direction} {measure.lower()} of {selected[measure]:,.2f}.",
            "steps": f"Grouped records by {group_column}, calculated total {measure.lower()}, and sorted the results.",
            "data": result
        }

    # STEP 7: Handle total calculations
    if any(word in question for word in ["total", "overall", "sum"]):

        total = df[measure].sum()

        if measure == "Quantity":
            formatted_total = f"{total:,.0f}"
        else:
            formatted_total = f"{total:,.2f}"

        return {
            "answer": f"Total {measure.lower()} is {formatted_total}.",
            "steps": f"Calculated the sum of the {measure} column.",
            "data": pd.DataFrame({
                "Metric": [f"Total {measure}"],
                "Value": [total]
            })
        }
