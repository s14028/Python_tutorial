from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(11)

dataset = np.loadtxt("dataset.txt", delimiter=",")
input = dataset[:, 0:8]
output = dataset[:, 8]

activation_function = {"hard_sigmoid", "sigmoid", "linear", "tanh", "softsign", "softplus", "selu", "elu", "softmax", "relu"}
scores = []


for i in range(30):
    for function_name in activation_function:
        model = Sequential()
        model.add(Dense(12, input_dim=8, kernel_initializer="uniform", activation="relu"))
        model.add(Dense(8, activation=function_name))
        model.add(Dense(1, activation="sigmoid"))
        
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
        model.fit(input, output, epochs=300, batch_size=10, verbose=0)
        scores.append(model.evaluate(input, output)[1] * 100)
    
    result = zip(activation_function, scores)
    with open("log/log_{}.txt".format(str(i)), "w") as file:
        for function_name, score in result:
            file.write("{} = {}\n".format(function_name, score))

    scores = []
