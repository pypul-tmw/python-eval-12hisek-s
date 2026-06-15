import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('example.csv')

avg_age = data.groupby('gender')['age'].mean()
avg_age.plot(kind="bar", title="Average age by gender")

plt.xlabel("Gender")
plt.ylabel("Average Age")

plt.savefig("plot.png")   # instead of plt.show()