map = {
	'a' : 1,
	'b' : 2
	}
for i, w in enumerate(map):
	print("{} -> {}".format(i, w))
for i, q in map.items():
	print("{} -> {}".format(i, q))

boolList = [True] * 100
print(all(boolList))

boolList = [False] * 100
boolList[99] = True
print(any(boolList))

w = [i for i in range(11)]
del w[0:3]
print(w)

print(len(w))

print(w[0:5:2])

print(w[-1:])

print(w[:-1])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotation = zip(*matrix)


print(*matrix, sep='\n')
array = [i for i in reversed(range(11))]
print(*array, sep=' ')
