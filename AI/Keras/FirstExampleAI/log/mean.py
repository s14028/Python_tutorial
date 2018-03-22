prefix = "log_"

names = []
accuracies = [0 for i in range(10)]

with open(prefix + "0.txt", "r") as file:
    for i in file.readlines():
        names.append(i.split(" = ")[0])

for i in range(11):
    file_name = prefix + str(i) + ".txt"
    with open(file_name, "r") as file:
        lines = file.readlines()
        for j, r in enumerate(lines):
            accuracy = r.split(" = ")[1]
            accuracies[j] += float(accuracy)

accuracies = [i / 10 for i in accuracies]
elements = zip(names, accuracies)


for i, j in elements:
    print(i + " " + str(j))
