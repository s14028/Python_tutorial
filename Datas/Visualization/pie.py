import matplotlib.pyplot as plt

proportions = [0.2, 0.3, 0.5]
names = ["A", "B", "C"]

plt.pie(proportions, labels=names, shadow=False, colors=["blue", "red", "yellow"])

plt.tight_layout()
plt.show()
