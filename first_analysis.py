import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/Sample - Superstore.csv")
# Convert mixed date formats into datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="mixed", dayfirst=False
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="mixed", dayfirst=False
)
# Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display dataset dimensions
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())
print("\nDATA TYPES:")
print(df.dtypes)

print("\nORDER DATE SAMPLES:")
print(df["Order Date"].head(10))

print("\nUPDATED DATE TYPES:")
print(df[["Order Date", "Ship Date"]].dtypes)

print("\nCONVERTED ORDER DATES:")
print(df["Order Date"].head())


# Create additional date columns
df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month

df["Year-Month"] = df["Order Date"].dt.to_period("M")

# Display new columns
print("\nNEW DATE COLUMNS:")
print(df[["Order Date", "Year", "Month", "Year-Month"]].head(10))


# BASIC BUSINESS ANALYSIS

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()

print("\n===== BUSINESS SUMMARY =====")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Average Sales:", round(average_sales, 2))


# SALES AND PROFIT BY CATEGORY

category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

print("\n===== CATEGORY ANALYSIS =====")
print(category_analysis.round(2))


# SALES AND PROFIT BY REGION

region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

print("\n===== REGION ANALYSIS =====")
print(region_analysis.round(2))


# SALES AND PROFIT BY STATE

state_analysis = df.groupby("State").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

state_analysis = state_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\n===== TOP 10 STATES BY SALES =====")
print(state_analysis.head(10).round(2))



# MONTHLY SALES ANALYSIS

monthly_analysis = df.groupby("Year-Month").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

monthly_analysis["Year-Month"] = (
    monthly_analysis["Year-Month"].astype(str)
)

print("\n===== MONTHLY SALES ANALYSIS =====")
print(monthly_analysis.head(12).round(2))