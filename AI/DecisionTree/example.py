import pandas as ps
from sklearn.tree import DecisionTreeClassifier

df = ps.read_csv('input.csv', header=None)
output = df[3]

print(df)
print(output)
print(df.loc[:, 0:2])

tree = DecisionTreeClassifier()
tree = tree.fit(df.loc[:, 0:2], output)
prediction = tree.predict([[1, 151, 2]])

print(prediction)
