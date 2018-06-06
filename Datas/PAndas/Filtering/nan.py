import pandas as pd
import numpy as np
frame = pd.read_csv("data.csv", names=list("AWD"))
frame['R'] = pd.Series([np.nan for i in range(3)], index=frame.index)
print(frame)
print(frame.dropna(axis=1))
frame.iloc[:, 3].fillna(0, inplace=True)

frame.iloc[:, 3].fillna(pd.Series(data=[1, 2, 3]), inplace=True)
#Its must be the same size as an array, not the size of nans.
print(frame)

series = pd.Series(data=[1, np.nan, 3], name="A")

print(series.interpolate())

#Look for nans

nulls = series.isnull()

print(nulls)

print(nulls.sum())
