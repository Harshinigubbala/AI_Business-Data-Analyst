import pandas as pd


def load_data():
    df = pd.read_csv("data/raw/Sample - Superstore.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"], format="mixed"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"], format="mixed"
    )

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Year-Month"] = df["Order Date"].dt.to_period("M")

    return df


def get_business_summary(df):
    return {
        "Total Sales": float(round(df["Sales"].sum(), 2)),
        "Total Profit": float(round(df["Profit"].sum(), 2)),
        "Total Quantity": int(df["Quantity"].sum()),
        "Total Orders": int(df["Order ID"].nunique())
    }


def get_category_analysis(df):
    return df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    ).reset_index()


def get_region_analysis(df):
    return df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    ).reset_index()


def get_state_analysis(df):
    return df.groupby("State").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    ).reset_index().sort_values(
        by="Total_Sales", ascending=False
    )


def get_monthly_analysis(df):
    result = df.groupby("Year-Month").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    ).reset_index()

    result["Year-Month"] = result["Year-Month"].astype(str)

    return result


# TEST THE ANALYSIS FUNCTIONS
if __name__ == "__main__":
    df = load_data()

    print("\n===== BUSINESS SUMMARY =====")
    print(get_business_summary(df))

    print("\n===== CATEGORY ANALYSIS =====")
    print(get_category_analysis(df).round(2))