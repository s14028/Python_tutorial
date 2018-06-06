import pandas as pd

data = pd.Series(data=[i for i in range(101) for j in range(2)])

print(pd.cut(data, 5))
print(pd.qcut(data, 5))
