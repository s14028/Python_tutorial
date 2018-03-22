def plus_number(array, number):
	for i in array:
		yield(i+number)

def print_array(array):
	for i in array:
		print i

def main():
	array = [1, 2, 3]
	array = plus_number(array, 5)
	'''In this place the array is an active generator.'''
	print_array(array)
	'''I have initialized array as list again, otherwise i won't be able to build another 
		 generator by using one up there. Can't perform yield with iterator.'''
	array = [5, 7, 9]
	array = (x + 5 for x in array)
	print "Next iterator"
	print_array(array)
	print "Another iterator {}".format(2)
	array = (x for x in [1, 2, 3]) 
	print_array(array)
if __name__ == "__main__":

	main()
