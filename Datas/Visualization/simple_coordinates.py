from pylab import *
import matplotlib.pyplot as plt

x = [0,2,-3,-1.5]
y = [0,3,1,-2.5]
color=['m','g','r','b']

fig = plt.figure()
ax = fig.add_subplot(111)

scatter(x,y, s=100 ,marker='o', c=color)

left,right = ax.get_xlim()
low,high = ax.get_ylim()
arrow(left, 0, right-left, 0, length_includes_head = True, head_width = 0.15)
arrow(0, low, 0, high-low, length_includes_head = True, head_width = 0.15) 

grid()
show()
