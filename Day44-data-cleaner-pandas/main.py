# Day 44 - Data Cleaner
# Concept: Pandas
# Goal: Practice loading, inspecting, and cleaning messy real-world data with pandas

# Requires: pip install pandas
import pandas as pd
import numpy as np

# --- Creating a messy sample dataset (in a real project, you'd load a CSV) ---
messy_data = {
    "Name": ["Kalid", "Asha", "Ravi", None, "Meera", "Kalid"],
    "Age": [30, 25, None, 40, 35, 30],
    "City": ["Bengaluru", "Mumbai", "Delhi", "Chennai", None, "Bengaluru"],
    "Salary": [50000, 60000, 55000, None, 70000, 50000],
}

df = pd.DataFrame(messy_data)   # a DataFrame is pandas' core structure - like a spreadsheet/table
print("--- Raw messy data ---")
print(df)

# --- Basic inspection - the FIRST things you do with any new dataset ---
print("\n--- .info() - column types and non-null counts ---")
df.info()

print("\n--- .describe() - summary statistics for numeric columns ---")
print(df.describe())

print("\n--- .shape - (rows, columns) ---")
print(df.shape)

print("\n--- .columns - list of column names ---")
print(df.columns.tolist())

# --- Checking for missing values ---
print("\n--- Missing values per column ---")
print(df.isnull().sum())

# --- Dropping rows with ANY missing values ---
df_dropped = df.dropna()
print("\n--- After dropna() (removes rows with any missing value) ---")
print(df_dropped)

# --- Filling missing values instead of dropping them ---
df_filled = df.copy()   # .copy() avoids modifying the original by accident
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Name"] = df_filled["Name"].fillna("Unknown")
df_filled["City"] = df_filled["City"].fillna("Unknown")
df_filled["Salary"] = df_filled["Salary"].fillna(df_filled["Salary"].median())

print("\n--- After filling missing values ---")
print(df_filled)

# --- Removing duplicate rows ---
print("\n--- Checking for duplicates ---")
print(df_filled.duplicated())

df_no_duplicates = df_filled.drop_duplicates()
print("\n--- After drop_duplicates() ---")
print(df_no_duplicates)

# --- Selecting a single column (returns a Series, pandas' 1D structure) ---
print("\n--- Selecting one column ---")
print(df_no_duplicates["Name"])
print("Type:", type(df_no_duplicates["Name"]))

# --- Selecting multiple columns (returns a DataFrame) ---
print("\n--- Selecting multiple columns ---")
print(df_no_duplicates[["Name", "Salary"]])

# --- Filtering rows based on a condition ---
print("\n--- People older than 30 ---")
print(df_no_duplicates[df_no_duplicates["Age"] > 30])

# --- Sorting ---
print("\n--- Sorted by Salary (descending) ---")
print(df_no_duplicates.sort_values("Salary", ascending=False))

# --- Adding a new column based on existing ones ---
df_no_duplicates["Salary_in_thousands"] = df_no_duplicates["Salary"] / 1000
print("\n--- After adding a calculated column ---")
print(df_no_duplicates)

# --- Renaming columns ---
df_renamed = df_no_duplicates.rename(columns={"Salary_in_thousands": "Salary (K)"})
print("\n--- After renaming a column ---")
print(df_renamed.columns.tolist())

# --- Grouping and aggregating - a very common real-world operation ---
print("\n--- Average salary by city ---")
print(df_no_duplicates.groupby("City")["Salary"].mean())

# --- Applying a function to a column ---
df_no_duplicates["Name_upper"] = df_no_duplicates["Name"].apply(lambda name: name.upper())
print("\n--- After applying a function to a column ---")
print(df_no_duplicates[["Name", "Name_upper"]])

# --- Saving the cleaned data back to a CSV file ---
df_no_duplicates.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved to cleaned_data.csv")

# --- Reading it back to confirm ---
reloaded = pd.read_csv("cleaned_data.csv")
print("\n--- Reloaded from CSV ---")
print(reloaded)