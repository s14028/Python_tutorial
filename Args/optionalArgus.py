import argparse

def sum(args):
	sum = 0
	for i in args:
		sum += i
	return sum

def main():
	parser = argparse.ArgumentParser("Optional arguments tutorial.")
	'''When you are having optional arguments set name and default value.'''
	parser.add_argument("-f", "--first", dest = "first", default = "Def", type = str, help = "First argument required.")
	parser.add_argument("-w", "--arguments", dest = "W", type = int, default = [], nargs = "*", help = "Array ints sum.")
	args = parser.parse_args()
	print(args.first)
	array = args.W
	print(sum(array))
		
if __name__ == "__main__":
	main()
