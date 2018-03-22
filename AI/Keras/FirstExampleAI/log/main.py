import math

names = ["" for i in range(10)]
elements = []

file_name = "log_{}.txt".format(0)
with open(file_name, "r") as file:
    lines = file.readlines()
    for i, j in enumerate(lines):
        names[i] = j.split(" = ")[0]

for i in range(19):
    file_name = "log_{}.txt".format(str(i))
    elements.append(list())
    with open(file_name, "r") as file:
        lines = file.readlines()
        for j in lines:
            value = j.split(" = ")[1]
            elements[i].append(float(value))

means = [0 for i in range(10)]

for i in range(10):
    for j in elements:
        means[i] += j[i]

means = [i/19 for i in means]
stdvn = [0 for i in range(10)]

for i in range(10):
    for j in elements:
        stdvn[i] += (j[i] - means[i]) ** 2

stdvn = [math.sqrt(i/18) for i in stdvn]
a = 0.05
t = 2.1009
left_right = [[means[i] - t * stdvn[i]/math.sqrt(19), means[i] + t * stdvn[i]/math.sqrt(19)] for i in range(10)]

result = zip(names, left_right)

print(max(result, key=lambda x: x[1][0]))
