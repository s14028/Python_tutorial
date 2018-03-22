import pandas as pd

frame = pd.read_csv("adata.csv", header=None, names=['a', 'b', 'c'])

max_value_in_a = frame['a'].max()
print(max_value_in_a)

#Another way of recieving this:
sort = frame.sort_values(['a'], ascending=False)
print(sort) #A view to data set.
print(frame)
