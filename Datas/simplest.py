import pandas
import random

ds = {"weight" : [1, 2, 3, 4, 5, 4, 3, 4, 3, 4, 3],
			"height" : [100, 300, 200, 100, 100, 100, 11, 3, 9, 1, 11]}

visualization = pandas.DataFrame(ds)
print(visualization.describe())

print(visualization)

print(visualization[visualization.height > 100])
print(visualization[visualization.height == visualization.height.max()])
print(visualization[visualization.height == visualization.height.min()])

visualization += [1, 500]

print(visualization)

array = [random.randint(0, 10) for i in range(101)]

visualization = pandas.Series(array)
print(visualization.value_counts())

print(visualization.mode())

visualization.to_csv("test.csv")
