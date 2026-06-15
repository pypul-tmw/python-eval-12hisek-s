import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df)