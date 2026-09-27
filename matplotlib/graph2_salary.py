import matplotlib.pyplot as plt
import pandas as pd
data= {
    "salary" :[25000 , 30000 , 35000 , 29000 , 36000 , 40000]
}
data_frame = pd.DataFrame(data)
print(data_frame)
plt.plot(data ["salary"] , color="green" , marker="o", linestyle="--" )
plt.grid(True)
plt.show()

