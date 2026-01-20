Code-1

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(np.mean(a))
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(a.reshape(2, 2))
print(a[2])
print(a[1:3])
print(a > 2)
print(a[a > 2])
print(np.sort(b))
print(np.random.randint(1, 10, (2, 2)))

Code-2

import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, 22, 23],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print(df)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df["Marks"])
print(df[["Name", "Age"]])
print(df.loc[1])
print(df.iloc[2])
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())
print(df[df["Marks"] > 80])

df["Passed"] = df["Marks"] >= 80
print(df)

print(df.sort_values("Marks"))


Code-3

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Line graph
plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("line_graph.png")
plt.close()

# Bar chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("bar_chart.png")
plt.close()

# Scatter plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("scatter_plot.png")
plt.close()

# Pie chart
labels = ["A", "B", "C", "D"]
sizes = [30, 25, 25, 20]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.savefig("pie_chart.png")
plt.close()

# Histogram
data = [10, 20, 20, 30, 30, 30, 40, 50, 50]

plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()
