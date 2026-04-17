import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/cleaned_expenses.csv")

sns.set(style="whitegrid")

# -----------------------------
# 1. Category-wise Spending
# -----------------------------
category_spend = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=category_spend.index, y=category_spend.values)
plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.savefig("images/category_spending.png")
plt.show()

# -----------------------------
# 2. Expense Distribution (Pie)
# -----------------------------
plt.figure(figsize=(6,6))
plt.pie(category_spend, labels=category_spend.index, autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.savefig("images/pie_chart.png")
plt.show()

# -----------------------------
# 3. Monthly Trend
# -----------------------------
df['Month_Num'] = pd.to_datetime(df['Date']).dt.month

monthly = df.groupby('Month_Num')['Amount'].sum()

plt.figure(figsize=(8,5))
monthly.plot(marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.savefig("images/monthly_trend.png")
plt.show()

# -----------------------------
# 4. Transactions by Weekday
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x='Weekday', data=df,
              order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
plt.title("Transactions by Weekday")
plt.xticks(rotation=45)
plt.savefig("images/weekday_transactions.png")
plt.show()
# -----------------------------
# 5. Insights Generation
# -----------------------------

print("\n📊 KEY INSIGHTS:")

# Highest spending category
category_spend = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
print("💸 Highest Spending Category:", category_spend.idxmax())

# Lowest spending category
print("💰 Lowest Spending Category:", category_spend.idxmin())

# Total expense
total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
print("📉 Total Expense:", total_expense)

# Total income
total_income = df[df['Type'] == 'Income']['Amount'].sum()
print("📈 Total Income:", total_income)

# Savings
savings = total_income - total_expense
print("💼 Net Savings:", savings)