import pickle

with open("saveObject.txt", "rb") as file:
	array = pickle.load(file)
	print(array[:])
