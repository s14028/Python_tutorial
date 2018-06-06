import pandas as pd

def find_max(row):
    max_value = row.max()
    row.loc[:, "O"] = max_value

    return row

data = {"A": [1, 2, 3], "B": [2, 3, 4]}
data = pd.DataFrame(data=data)
data.iloc[:, "O"] = 0

data.apply(find_max, axis=1, inplace=True)

print(data)
