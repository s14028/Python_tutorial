import pandas as pd
import numpy as np
frame = pd.read_csv("data.csv", names=list('ADR'))
frame.iloc[0, 2] = np.nan
print(frame)

mask = (frame['A'] > 1) & (frame['D'] == 't')
#Removes rows which not covered up by criteria.
print(frame.loc[mask])
#Places NaN rows to stick to size.
print(frame.where(mask))
#Replces all rows which had False with NaN.
print(frame.where(mask, np.nan))


#Where always creates a copy of data set. In order to prevent it use inplace.
frame.where(mask | (frame['A'] == 1), inplace=True)

print(frame)

grouped = frame.groupby('A')
grouped = frame.groupby(['A', 'D'], sort=True)
print(grouped.groups)
