import pandas as pd

frame = pd.DataFrame(data={"A": [1, 2, 3], "B": [1., 2., 3.], "C": ["a", "b", "c"]})

for name, df in frame.groupby("C"):
	print(df.iloc[:, :-1].mean())
	print(name)
	print(df)

