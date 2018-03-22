import pandas as pd

series = pd.Series([1, 2, 3, 'a', 1., True, []], name="A") # ndarray
frame = pd.DataFrame(data=list(zip([1, 2, 3], ['a', 'b', 'c'])), columns=list('AR'))
frame = pd.DataFrame(data={'A' : [1, 2, 3], 'D' : ['a', 'b', 'c']})
