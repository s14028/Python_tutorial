import pandas as pd

frame = pd.read_csv("data.csv", names=list('ADR'))

print(frame[frame['A'] > 1]) #Could return a copy.
print(frame.loc[frame['A'] > 1, ['A', 'D']]) #Guaranted to be in place.


mask = (frame['A'] > 1) & (frame['D'] == 't')
print(frame.loc[mask, ['A']])
print(frame[mask])

print(frame.loc[frame['A'] == frame['A'].max(), ['A', 'D']])
