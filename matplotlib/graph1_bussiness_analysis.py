import matplotlib.pyplot as plt
x=[1,2,3,4,5] # months
y=[10000,23000,34000,25000,27000] #revenue
plt.title("Bussiness Analysis")
plt.xlabel("months")
plt.ylabel("revenue")
plt.plot(x,y , color="red" , marker="o")
plt.grid(True)
plt.show()
