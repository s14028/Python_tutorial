def positionalArgs(*args):
	print(args)
	for i in args:
		print(i)

positionalArgs(1, 2, 3)

array = [1, 2, 3]
positionalArgs(array)
positionalArgs(*array)
