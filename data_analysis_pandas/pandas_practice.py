import pandas as pd


data = {
    "Name":["John","Ash","Bob"],
    "Age": [25, 30, 22],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df)
print(df.head(1))
print(df.tail(1))
print(df.shape)
print(df.columns)