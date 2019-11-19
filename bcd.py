import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# Create figure and axes
fig, ax = plt.subplots(1)

color = {0: "r", 1: "g", 2: "b", 3: "b" }
x = 0
y = 0
rank = 0
size = 32
dim = 1560
numprocs = 4

dix = size
diy = size
numof = int((dim/size) + 0.5) + 1

startrank = 0
x = 0
for i in range(0,numof):
    y = 0

    for j in range(0,numof):
      rect = Rectangle((y,x),diy,dix,
              linewidth=0,edgecolor=color[rank],
              facecolor=color[rank])
      ax.add_patch(rect)

      rank += 1
      if (rank >= (numprocs/2)):
        rank = startrank
      y += 32

    break

    startrank += (numprocs/2)
    if (startrank >= numprocs):
        startrank = 0

    x += 32


ax.set(xlim=(0, dim), ylim=(0, dim))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

plt.show()
