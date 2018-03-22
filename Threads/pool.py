from multiprocessing import Pool

def fib(x):
	if x == 0: return 0;
	if x == 1: return 1;
	return fib(x - 1) + fib(x - 2)

def main():
	pCount = 8
	inArray = [x + 1 for x in range(5)]
	with Pool(pCount) as pool:
		pool.map(fib, inArray)


if __name__ == "__main__":
	main()
