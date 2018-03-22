import matplotlib.pyplot as pt
import numpy as np

x0, y0 = [1, 2, 3], [5, 7, 9]
x1, y1 = [0, 1, 2], [4, 5, 7]

pt.plot(x0, y0, label="Label")
pt.plot(x1, y1, label="Wounderfulabel")

pt.xlabel("X")
pt.ylabel("y")
pt.legend()
pt.title("A")
pt.savefig("output.pdf")

pt.show()
pt.close()

average, sigma = 0, 1

data = np.random.normal(average, sigma, 10000)

pt.hist(data, bins=50, normed=1)

pt.show()
pt.close()

poisson = np.random.poisson(35, 10000)
exponential = np.random.exponential(35, 10000)

pt.subplot(2, 1, 1)

pt.hist(poisson, bins=50, normed=1)
pt.title("Poisson")

pt.subplot(2, 1, 2)
pt.hist(exponential, bins=50, normed=1)
pt.title("Exponential")
pt.show()
