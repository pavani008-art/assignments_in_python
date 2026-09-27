import pandas as pd

data = {
    "Name": ["Ravi", "Sita", "Rahul", "Anu", "Kiran", "Priya", "Arjun"],
    "Age": [18, 19, 18, 20, 19, 18, 19],
    "Marks": [85, 72, 90, 65, 55, 78, 88],
    "Course": ["BSc", "BCA", "BSc", "BCom", "BCA", "BSc", "BCA"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nNumber of rows and columns:")
print(df.shape)

print("\nTotal cells:")
print(df.size)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 4 rows:")
print(df.tail(4))