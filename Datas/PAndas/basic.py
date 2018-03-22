import pandas as pd

x = [1, 2, 3]
y = ['a', 'b', 'w']
frame = pd.DataFrame(data=list(zip(x, y)), columns=['X', 'Y'])

print(frame.head())
