import pandas as pd

frame = pd.DataFrame(columns=["Name", "Age"], index=["A", "B"])
frame.loc["A", "Name"] = "Adam"
frame.loc["A", "Age"] = 1

frame.drop("B", inplace=True)

B = pd.Series(data=["B", 1], index=["Name", "Age"])
frame = frame.append(B, ignore_index=True) # Koniecznie trzeba przypisac do zmiennej, inaczej sie nie powiedzie
frame = frame.append({"Name" : "C", "Age" : 1}, ignore_index=True)

frame = frame.drop(index=[1])
frame = frame.drop(columns=["Name"])
print(frame)
