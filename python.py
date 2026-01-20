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
