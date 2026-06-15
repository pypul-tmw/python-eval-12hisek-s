import pandas as pd 

df = pd.read_csv("employee.csv")
high_salary = df[df["salary"] > 50000]

df["bonus"] = df["salary"] * 0.10




print(df)

print("Columns:\n",df.columns)

print("Tail:",df.tail(1))

print("Highest Salary:\n",high_salary)

#checking missing values
print(df.isnull().sum())

#fill missing value with mean
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["bonus"] = df["bonus"].fillna(df["bonus"].mean())
print(df)

df.to_excel("output.xlsx",index= False)