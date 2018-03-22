from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(11)

dataset = np.loadtxt("dataset.txt", delimiter=",")
input = dataset[:, 0:8]
output = dataset[:, 8]

#[:, 0:8] is numpy array signature and is equal to [:][0:8]
#when we are constructing model, we prefer to use Sequential, and now we can simply add layers to our network
#sequentialy

#Dense means that we are using fully connected layer
#Every layer could also recieve kernel initializer, which is a weight generator based on random value distribution
#Example: model.add(Dense(12, input_dim=8, kernel_initializer="uniform", activation="relu"))
#Or model.add(Dense(12, input_dim=8, kernel_initializer="normal", activation="relu"))

model = Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer="uniform", activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(input, output, epochs=300, batch_size=10)
scores = model.evaluate(input, output)

print(model.metrics_names[1], scores[1] * 100)

print(*model.metrics_names)
