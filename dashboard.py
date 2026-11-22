

import streamlit as st
import plotly.express as px

from qa_engine import answer_question

from analysis import (
    load_data,
    get_business_summary,
    get_category_analysis,
    get_region_analysis,
    get_state_analysis,
    get_monthly_analysis
)


# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Business Data Analyst",
    page_icon="📊",
    layout="wide"
)


# LOAD DATA
df = load_data()


# DASHBOARD TITLE
st.title("📊 AI-Powered Business Data Analyst")
st.write(
    "Explore business sales, profit, products and locations."
)


# SIDEBAR FILTERS
st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

years = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)


# APPLY FILTERS
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Year"].isin(years))
]


# BUSINESS SUMMARY
st.header("Business Summary")

summary = get_business_summary(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${summary['Total Sales']:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${summary['Total Profit']:,.2f}"
)

col3.metric(
    "Total Quantity",
    f"{summary['Total Quantity']:,}"
)

col4.metric(
    "Total Orders",
    f"{summary['Total Orders']:,}"
)


# CATEGORY ANALYSIS
st.header("Sales and Profit by Category")

category_data = get_category_analysis(filtered_df)

fig_category = px.bar(
    category_data,
    x="Category",
    y=["Total_Sales", "Total_Profit"],
    barmode="group",
    title="Category-wise Sales and Profit"
)

st.plotly_chart(fig_category, width="stretch")


# REGIONAL ANALYSIS
st.header("Regional Performance")

region_data = get_region_analysis(filtered_df)

fig_region = px.bar(
    region_data,
    x="Region",
    y="Total_Sales",
    title="Sales by Region",
    text_auto=".2s"
)

st.plotly_chart(fig_region, width="stretch")


# STATE ANALYSIS
st.header("Location-Based Analysis")

state_data = get_state_analysis(filtered_df).head(10)

fig_state = px.bar(
    state_data,
    x="Total_Sales",
    y="State",
    orientation="h",
    title="Top 10 States by Sales"
)

fig_state.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig_state, width="stretch")


# MONTHLY SALES ANALYSIS
st.header("Monthly Sales Trend")

monthly_data = get_monthly_analysis(filtered_df)

fig_monthly = px.line(
    monthly_data,
    x="Year-Month",
    y="Total_Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_monthly, width="stretch")


# DATA TABLE
st.header("Filtered Dataset")

st.dataframe(
    filtered_df,
    width="stretch"
)


# NATURAL LANGUAGE QUESTION ANSWERING
st.header("Ask Your Business Data")

# REMEMBER PREVIOUS QUESTIONS
if "previous_question" not in st.session_state:
    st.session_state.previous_question = None

user_question = st.text_input(
    "Enter your business question:",
    placeholder="Example: Which category has the highest sales?"
)


if st.button("Get Answer"):

    if user_question.strip():

        result = answer_question(
            filtered_df,
            user_question,
            st.session_state.previous_question
        )

        # DISPLAY ANSWER
        st.subheader("Answer")
        st.success(result["answer"])

        # DISPLAY ANALYSIS STEPS
        st.subheader("Analysis Steps")
        st.write(result["steps"])

        # DISPLAY SUPPORTING RESULTS
        if result["data"] is not None:

            st.subheader("Supporting Results")

            st.dataframe(
                result["data"],
                width="stretch"
            )

            # SAVE SUCCESSFUL QUESTION CONTEXT
            st.session_state.previous_question = user_question

    else:
        st.warning("Please enter a question.")


# FOOTER
st.caption(
    "AI-Powered Business Data Analyst | "
    "Built using Python, Pandas, Streamlit and Plotly"
)
