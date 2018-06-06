import pandas as pd

series = pd.Series([1, 2, 3, 'a', 1., True, []], name="A") # ndarray
for i in series:
	print(i)
frame = pd.DataFrame(data=list(zip([1, 2, 3], ['a', 'b', 'c'])), columns=list('AR'))

for i in frame.columns:
	print(i)

frame = pd.DataFrame(data={'A' : [1, 2, 3], 'D' : ['a', 'b', 'c']})
