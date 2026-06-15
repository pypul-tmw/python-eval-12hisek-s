import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('example_data.csv')

avg_age_by_gender = 
(
    data.groupby('gender')['age'].mean().sort_values()
)
avg_age_by_gender.plot(kind="bar",title="Average age by gender")
plt.xlabel('Gender')
plt.ylabel('Average Age')
plt.savefig("output.png")