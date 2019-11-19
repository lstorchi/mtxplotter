import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# Create figure and axes
fig, ax = plt.subplots(1)

xmin = 0
ymin = 0
xmax = 0
ymax = 0
fp = open("data.txt")
color = {0: "r", 1: "g", 2: "b", 3: "b" }
idx = 0
for line in fp:
    idx += 1
    sline = line.split()

    if (len(sline) != 6):
        print "Error t line ", idx
        exit(1)

    rank = int(sline[1])

    x = int(sline[2])
    y = int(sline[3])

    if (x < xmin):
        xmin = x
    if (x > xmax):
        xmax = x

    if (y < ymin):
        ymin = y
    if (y > ymax):
        ymax = y

    dix = int(sline[4])
    diy = int(sline[5])

    rect = Rectangle((x,y),dix,diy,
            linewidth=0,edgecolor=color[rank],facecolor=color[rank])

    ax.add_patch(rect)

ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
plt.axis('off')

fp.close()

plt.show()
