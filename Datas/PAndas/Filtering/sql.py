import pandas as pd
import numpy as np

left = {"A": [1, 2], "B": ['a', 'b']}
right = {"A": [2, 3], "B": ['c', 'd']}

a = pd.DataFrame(data=left)
b = pd.DataFrame(data=right)

print(a.join(b, lsuffix="_l", rsuffix="_r"))

left = {"A": [1, 2, 3], "B": ['a', 'b', 'd']}
right = {"C": [3, 5, 7], "D": ['d', 'r', 'a']}

indexes = ["a1", "b1"]

a = pd.DataFrame(data=left, index=indexes + ["c3"])
b = pd.DataFrame(data=right, index=indexes + ["d3"])

print(a.join(b, how="inner"))

print(a.join(b, how="left"))
print(a.join(b, how="right"))
print(a.join(b, how="outer"))

left = [1, np.nan, 3]
right = [0, 2, 1]

a = pd.Series(data=left)
b = pd.Series(data=right)
print(a.combine_first(b))
