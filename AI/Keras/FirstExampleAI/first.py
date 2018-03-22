from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(11)

dataset = np.loadtxt("dataset.txt", delimiter=",")
input = dataset[:, 0:8]
output = dataset[:, 8]

model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer="uniform", activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(input, output, epochs=300, batch_size=10)
scores = model.evaluate(input, output)

print(model.metrics_names[1], scores[1] * 100)

print(*model.metrics_names)
#Suppose, that you already built up your model for specific problem, and now you have to save it in order to use later
#Use function save(file) in order to save weights of your model.
file_path = "weights"
model.save(file_path)
#You can later bring your weights after you will renew your model

model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer="uniform", activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.load_weights(file_path)
#Now you don't have to train it again.
