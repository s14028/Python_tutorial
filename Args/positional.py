import argparse

def main():
	parser = argparse.ArgumentParser("Positional arguments tutorial.")
	'''When you are having positional arguments they are always required.'''
	parser.add_argument("first", type = str, help = "First argument required.")
	args = parser.parse_args()
	print args.first
if __name__ == "__main__":
	main()
