import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/cleaned_expenses.csv")

# Title
st.title("💰 Expense Tracker Dashboard")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Category-wise spending
st.subheader("📊 Category-wise Spending")
category = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
st.bar_chart(category)

# Monthly trend
st.subheader("📈 Monthly Trend")
df['Month_Num'] = pd.to_datetime(df['Date']).dt.month
monthly = df.groupby('Month_Num')['Amount'].sum()
st.line_chart(monthly)

# Insights
st.subheader("📌 Key Insights")

total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
total_income = df[df['Type'] == 'Income']['Amount'].sum()

st.write("💸 Total Expense:", total_expense)
st.write("📈 Total Income:", total_income)
st.write("💼 Savings:", total_income - total_expense)