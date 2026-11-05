# Day 45 - Graph Plotter
# Concept: Matplotlib
# Goal: Practice creating different types of charts/plots using matplotlib

# Requires: pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# --- Sample data to plot ---
days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [25, 27, 24, 30, 28, 26, 29]

# --- A basic LINE plot ---
plt.plot(days, temperatures)
plt.title("Temperature Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.savefig("line_plot.png")   # saves the chart as an image file
plt.show()                     # displays it in a window
plt.close()                    # closes the figure so the next plot starts fresh

# --- Styling a line plot: color, marker, line style ---
plt.plot(days, temperatures, color="red", marker="o", linestyle="--", label="Bengaluru")
plt.title("Styled Line Plot")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()   # shows the label defined above
plt.grid(True)   # adds a background grid
plt.savefig("styled_line_plot.png")
plt.show()
plt.close()

# --- Plotting MULTIPLE lines on the same chart ---
city_a_temps = [25, 27, 24, 30, 28, 26, 29]
city_b_temps = [22, 23, 25, 24, 26, 27, 25]

plt.plot(days, city_a_temps, label="Bengaluru", marker="o")
plt.plot(days, city_b_temps, label="Mumbai", marker="s")
plt.title("Temperature Comparison")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.savefig("multi_line_plot.png")
plt.show()
plt.close()

# --- A BAR chart - good for comparing categories ---
cities = ["Bengaluru", "Mumbai", "Delhi", "Chennai"]
avg_temps = [26, 29, 32, 31]

plt.bar(cities, avg_temps, color="skyblue")
plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.savefig("bar_chart.png")
plt.show()
plt.close()

# --- A horizontal bar chart ---
plt.barh(cities, avg_temps, color="lightgreen")
plt.title("Average Temperature by City (Horizontal)")
plt.savefig("horizontal_bar_chart.png")
plt.show()
plt.close()

# --- A PIE chart - good for showing proportions of a whole ---
categories = ["Food", "Transport", "Bills", "Entertainment"]
spending = [30, 20, 35, 15]

plt.pie(spending, labels=categories, autopct="%1.1f%%")   # autopct shows percentages
plt.title("Monthly Spending Breakdown")
plt.savefig("pie_chart.png")
plt.show()
plt.close()

# --- A SCATTER plot - good for showing relationships between two variables ---
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 70, 78, 85, 90]

plt.scatter(study_hours, exam_scores, color="purple")
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.savefig("scatter_plot.png")
plt.show()
plt.close()

# --- A HISTOGRAM - good for showing the distribution of a single variable ---
random_scores = np.random.normal(70, 10, 200)   # 200 values, mean=70, std=10

plt.hist(random_scores, bins=20, color="orange", edgecolor="black")
plt.title("Distribution of Test Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()
plt.close()

# --- Subplots - multiple charts in ONE figure ---
fig, axes = plt.subplots(2, 2, figsize=(10, 8))   # a 2x2 grid of charts

axes[0, 0].plot(days, temperatures)
axes[0, 0].set_title("Line Plot")

axes[0, 1].bar(cities, avg_temps)
axes[0, 1].set_title("Bar Chart")

axes[1, 0].pie(spending, labels=categories, autopct="%1.1f%%")
axes[1, 0].set_title("Pie Chart")

axes[1, 1].scatter(study_hours, exam_scores)
axes[1, 1].set_title("Scatter Plot")

plt.tight_layout()   # prevents charts from overlapping each other
plt.savefig("subplots.png")
plt.show()
plt.close()

print("\nAll charts have been saved as .png files in this folder.")


# ============================================================
# A reusable function to plot any simple line chart
# ============================================================
def plot_line_chart(x_values, y_values, title, x_label, y_label, filename):
    plt.plot(x_values, y_values, marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()
    plt.close()


# --- Interactive part: plot your own data ---
print("\n--- Create your own line chart ---")
num_points = int(input("How many data points? "))
values = [float(input(f"Value {i+1}: ")) for i in range(num_points)]
x_values = list(range(1, num_points + 1))

plot_line_chart(x_values, values, "My Custom Chart", "Point", "Value", "my_chart.png")
print("Saved as my_chart.png")