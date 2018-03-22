import pickle

array = [x for x in range(0, 133)]
with open("saveObject.txt", "wb") as file:
	pickle.dump(array, file)
