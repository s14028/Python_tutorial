import pandas as pd

data_frame = pd.read_csv("data.csv", header=None, names=['a', 'b', 'c']) #Option header=None is used to prevent pandas misstaking first row as head.
data_frame.to_csv("adata.csv", index=False, header=False) #index=True will take first columnt and take it as index, header=True doing same with first row.
print(data_frame)
