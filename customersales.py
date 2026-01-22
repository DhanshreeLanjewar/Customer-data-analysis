import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sales = pd.read_csv(r"C:\Users\dhans\Downloads\sales_data.csv")
churn = pd.read_csv(r"C:\Users\dhans\Downloads\customer_churn.csv")

# ================= SALES ANALYSIS =================
print("\n--- SALES ANALYSIS ---")

# Create Total Sales column
sales['TotalSales'] = sales['Quantity'] * sales['Price']

# Sales by product
sales_by_product = sales.groupby('Product')['TotalSales'].sum()
print("\nSales by Product:")
print(sales_by_product)

# ================= CUSTOMER CHURN ANALYSIS =================
print("\n--- CUSTOMER CHURN ANALYSIS ---")

# Churn count
churn_count = churn['Churn'].value_counts()
print("\nChurn Count:")
print(churn_count)

# Average monthly charges by churn
avg_charges = churn.groupby('Churn')['MonthlyCharges'].mean()
print("\nAverage Monthly Charges by Churn:")
print(avg_charges)

# ================= VISUALIZATION =================
# Bar chart showing churn distribution
churn_count.plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# ================= SUMMARY =================
print("\n--- PROJECT SUMMARY ---")
print("Sales data is used to identify best-selling products.")
print("Churn data helps analyze customer retention.")
print("Bar chart visualizes churn distribution clearly.")
