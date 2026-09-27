import matplotlib.pyplot as plt

employees = ["Ravi", "Priya", "Kiran", "Anu", "Rahul"]
salary = [25000, 30000, 28000, 35000, 32000]

plt.bar(employees, salary)

plt.title("Employee Salary Visualization")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()