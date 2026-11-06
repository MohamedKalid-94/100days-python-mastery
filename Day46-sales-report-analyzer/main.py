# Day 46 - Sales Report Analyzer
# Concept: Data Analysis
# Goal: Bring together pandas (Day44) and matplotlib (Day45) into a real
#       end-to-end data analysis workflow

# Requires: pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# --- Sample sales data (in a real project, this would be loaded from a CSV/database) ---
sales_data = {
    "Date": pd.date_range(start="2026-01-01", periods=30, freq="D"),
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"] * 6,
    "Category": ["Electronics"] * 30,
    "Region": ["North", "South", "East", "West", "North"] * 6,
    "Units_Sold": [5, 12, 8, 3, 15, 7, 10, 6, 4, 20, 9, 11, 5, 8, 13,
                   6, 14, 7, 9, 12, 4, 16, 10, 8, 11, 5, 13, 9, 7, 15],
    "Price": [50000, 20000, 15000, 50000, 20000] * 6,
}

df = pd.DataFrame(sales_data)
df["Revenue"] = df["Units_Sold"] * df["Price"]   # a calculated column, like Day44

print("--- Sample of the sales data ---")
print(df.head())   # .head() shows the first 5 rows by default

print("\n--- Dataset info ---")
df.info()

# ============================================================
# Step 1: Overall summary statistics
# ============================================================
print("\n--- Overall Summary ---")
print(f"Total revenue: ₹{df['Revenue'].sum():,.2f}")
print(f"Total units sold: {df['Units_Sold'].sum()}")
print(f"Average units sold per day: {df['Units_Sold'].mean():.2f}")
print(f"Best single day for units sold: {df['Units_Sold'].max()}")


# ============================================================
# Step 2: Revenue by product
# ============================================================
revenue_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n--- Revenue by Product ---")
print(revenue_by_product)

# --- Visualizing it with a bar chart ---
revenue_by_product.plot(kind="bar", color="skyblue", title="Revenue by Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()
plt.close()


# ============================================================
# Step 3: Revenue by region
# ============================================================
revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("\n--- Revenue by Region ---")
print(revenue_by_region)

revenue_by_region.plot(kind="pie", autopct="%1.1f%%", title="Revenue Share by Region")
plt.ylabel("")   # pie charts don't need a y-label
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()
plt.close()


# ============================================================
# Step 4: Sales trend over time
# ============================================================
daily_units = df.groupby("Date")["Units_Sold"].sum()
print("\n--- Daily units sold (first 5 days) ---")
print(daily_units.head())

daily_units.plot(kind="line", marker="o", title="Units Sold Over Time", figsize=(10, 4))
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.grid(True)
plt.tight_layout()
plt.savefig("units_over_time.png")
plt.show()
plt.close()


# ============================================================
# Step 5: Finding the best and worst performing products
# ============================================================
best_product = revenue_by_product.idxmax()   # .idxmax() gives the LABEL of the max value, not the value itself
worst_product = revenue_by_product.idxmin()

print(f"\nBest performing product: {best_product} (₹{revenue_by_product.max():,.2f})")
print(f"Worst performing product: {worst_product} (₹{revenue_by_product.min():,.2f})")


# ============================================================
# Step 6: Filtering for a deeper look - e.g. only high-value transactions
# ============================================================
high_value_sales = df[df["Revenue"] > 200000]
print(f"\n--- High-value transactions (Revenue > ₹200,000): {len(high_value_sales)} found ---")
print(high_value_sales[["Date", "Product", "Region", "Revenue"]])


# ============================================================
# Step 7: Pivot table - a powerful way to cross-tabulate data
# ============================================================
# Rows = Product, Columns = Region, Values = total Revenue
pivot = df.pivot_table(values="Revenue", index="Product", columns="Region", aggfunc="sum", fill_value=0)
print("\n--- Pivot Table: Revenue by Product and Region ---")
print(pivot)


# ============================================================
# Step 8: Exporting the final report
# ============================================================
summary_report = pd.DataFrame({
    "Total Revenue": [df["Revenue"].sum()],
    "Total Units": [df["Units_Sold"].sum()],
    "Best Product": [best_product],
    "Worst Product": [worst_product],
})

summary_report.to_csv("sales_summary_report.csv", index=False)
df.to_csv("full_sales_data.csv", index=False)

print("\nReports saved: sales_summary_report.csv, full_sales_data.csv")
print("Charts saved: revenue_by_product.png, revenue_by_region.png, units_over_time.png")