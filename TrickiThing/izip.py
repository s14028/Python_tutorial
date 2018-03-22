import itertools

arrayF = {1, 2, 3}
arrayS = {"a", "b"}

for x, y in itertools.izip(arrayF, arrayS):
	print("{}, {}".format(x, y))