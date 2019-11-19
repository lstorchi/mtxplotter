import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# Create figure and axes
fig, ax = plt.subplots(1)

color = {0: "r", 1: "g", 2: "b", 3: "y" }
rank = 0
size = 32
dim = 1560
numprocs = 4
dix = size
diy = size
numof = int((dim/size) + 0.5) + 1

startrank = 0
y = dim-32
for i in range(0,numof):
    x = 0
    rank = startrank
    maxproc = startrank + (numprocs/2)

    for j in range(0,numof):
      rect = Rectangle((x,y),dix,dix,
              linewidth=0,edgecolor=color[rank],
              facecolor=color[rank])
      ax.add_patch(rect)

      rank += 1
      if (rank >= maxproc):
        rank = startrank
      x += 32

    startrank += (numprocs/2)
    if (startrank >= numprocs):
        startrank = 0

    y -= 32


ax.set(xlim=(0, dim), ylim=(0, dim))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

plt.show()
