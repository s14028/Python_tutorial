from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(35)

dataset = np.loadtxt("z17.data.txt", delimiter=",")
input = dataset[:, :5]
output = dataset[:, 5:]

model = Sequential()

model.add(Dense(3, input_dim=5, kernel_initializer="uniform", activation="relu"))

model.add(Dense(2, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(input, output, epochs=500, batch_size=1, verbose=0)
model.save("file.txt")
