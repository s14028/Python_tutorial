import pandas as pd

x = [1, 2, 3]
y = ['a', 'b', 'c']
frame = pd.DataFrame(data=list(zip(x, y)), columns=list('AD'))
print(frame.iloc[0:2, 0])#Recieves rows from 0 to 2 and 0 columns.
print(frame.iloc[0, 0:1])#Recieves first row and columns from 0 to 1.
print(frame.iloc[0, 0])#Recieves specific value from 0 row 0 columns.
print(frame.iat[0, 0])#More effective way. Arguably could return value instead of reference if it's data type which is low level.
print(frame.loc[0:1, ['A']])#Under the hood looks like iloc, but recieves a name of rows and columns.
#loc, iloc will ensure that you would get a view of ds.
#When you will use simple brackets, it is not guaranted and copy could be returned.
print(frame.loc[(frame["A"] >= 2) | (frame["D"] == "a")])
