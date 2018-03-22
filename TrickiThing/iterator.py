import itertools

firstIter = [i for i in range(0, 1)]
lastIter = [i for i in range(1, 2)]

merge = itertools.chain(firstIter, lastIter)

iterators = itertools.chain.from_iterable(merge)


combinations = itertools.combinations([1, 2, 3, 4], 2)

def combine(array, count):
	for i in range(0, len(array) - count + 1):
		comb(array, [], count, i)

def comb(array, current, currentCount, index):
	current.append(array[index])
	copy = list(current)
	currentCount -= 1

	if currentCount == 0:
		print(current)
		return

	for i in range(index + 1, len(array) - currentCount + 1):
		comb(array, current, currentCount, i)
		current = copy
		copy = list(copy)
combine([1, 2, 3, 4], 2)

permutations = itertools.permutations([1, 2, 3, 4], 2)

product = itertools.product([1, 3], [1, 5, 9])

for i in combinations:
	print(i)
