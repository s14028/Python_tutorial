import sklearn.preprocessing as preprocessing

encoder = preprocessing.LabelEncoder()
encoder.fit(["a", "a", "b", "d", "c"])
print(encoder.classes_)

print(encoder.transform(["a", "b", "d"]))

print(encoder.inverse_transform([0, 1, 2]))

encoder.fit_transform(["dupa", "jas", "w"])

print(encoder.classes_)
