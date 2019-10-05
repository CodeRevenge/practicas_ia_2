# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
import sys
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pylab as plt
from matplotlib.figure import Figure
import numpy as np
from collections import deque
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter

    
class Points_Input(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)    
        ax = self.fig.add_subplot(111)
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])
        self.rojos = []
        self.azules = []
        self.linea = False
        self.x = np.arange(0,11)
        self.y = self.x
        self.canvas.setFocus()
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()
    
    def onclick(self, event):
        if self.linea:
            d = (event.xdata - 0)*(11-0) - (event.ydata-0)*(11-0)
            if d < 0:
                plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='b')
            else:
                plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='r')
        else:
            if int(event.button) == 1:
                plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='b')
                self.azules.append([event.xdata, event.ydata])
            elif int(event.button) == 3:
                plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='r')
                self.rojos.append([event.xdata, event.ydata])
            else:
                plt.plot(self.x,self.y, c='g')
                plt.fill_between(self.x, self.y, np.max(self.y), color='#539ecd')
                plt.fill_between(self.x, self.y, color='#e89a7d')
                plt.scatter(np.array(self.azules)[:,0],np.array(self.azules)[:,1], marker='o', c='b', s=10)
                plt.scatter(np.array(self.rojos)[:,0],np.array(self.rojos)[:,1], marker='o', c='r', s=10)
                self.linea = True

        self.canvas.draw()