import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
rojos = []
azules = []
linea = False
x = np.arange(0,11)
y = x

def onclick(event):
    global linea
    if linea:
        d = (event.xdata - 0)*(11-0) - (event.ydata-0)*(11-0)
        if d < 0:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='b')
        else:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='r')
    else:
        if int(event.button) == 1:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='b')
            azules.append([event.xdata, event.ydata])
        elif int(event.button) == 3:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='r')
            rojos.append([event.xdata, event.ydata])
        else:
            plt.plot(x,y, c='g')
            plt.fill_between(x, y, np.max(y), color='#539ecd')
            plt.fill_between(x, y, color='#e89a7d')
            plt.scatter(np.array(azules)[:,0],np.array(azules)[:,1], marker='o', c='b', s=10)
            plt.scatter(np.array(rojos)[:,0],np.array(rojos)[:,1], marker='o', c='r', s=10)
            linea = True

    fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()