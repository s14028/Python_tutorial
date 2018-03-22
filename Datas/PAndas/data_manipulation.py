import pandas as pd

data  = pd.read_csv("data.csv", header=None, names=None)

data.iloc[:, 0] += data.iloc[:, 0]

data.loc[:, "R"] = (data.iloc[:, 0] + 1).apply(lambda x: str(x) + 'a')

print(data)
