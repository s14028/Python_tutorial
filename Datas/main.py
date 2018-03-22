import pandas

input = pandas.read_csv("input", header=None, dtype=str) #nrows=3, na_values=["value", "echange with"], na_values={"column" : ["value", "exchange with"]}
input.columns = ["Id", "A", "B", "C", "D"]
print(input)
