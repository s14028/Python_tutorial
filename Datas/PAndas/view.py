import pandas as pd

frame = pd.Series(['a', 'b', 1, True, 1.], name='A')#A ndarray under the hood.

frame = pd.read_csv("data.csv", names=list('ADR'))

print(frame.head())
print(frame.tail(5))
print(frame.index)
print(frame.describe())
print(frame.T)
print(frame.sort_index(axis=1, ascending=True))
print(frame.sort_values(by='D'))
