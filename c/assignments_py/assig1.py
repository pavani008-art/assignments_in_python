bill_unit = int(input("Enter the units: "))

if bill_unit <= 100:
    bill = bill_unit * 5
elif bill_unit <= 200:
    bill = bill_unit * 7
elif bill_unit <= 300:
    bill = bill_unit * 10
else:
    bill = bill_unit * 12

print("Electricity Bill = ₹", bill)