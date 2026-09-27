import pandas as pd

data = {
    "Name": ["Ravi", "Sita", "Rahul", "Anu", "Kiran",
             "Priya", "Arjun", "Divya", "Vijay", "Sneha",
             "Rohit", "Pooja", "Aman", "Keerthi", "Manoj"],

    "Age": [18, 19, 18, 20, 19, 18, 19, 20, 18, 19, 
            20, 18, 19, 20, 18],

    "Marks": [85, 72, 90, 65, 55, 78, 88, 69, 92, 74,
              81, 60, 95, 70, 67],

    "Course": ["BSc", "BCA", "BSc", "BCom", "BCA",
               "BSc", "BCA", "BSc", "BCom", "BSc",
               "BCA", "BCom", "BSc", "BCA", "BSc"]
}

df = pd.DataFrame(data)

print(df)