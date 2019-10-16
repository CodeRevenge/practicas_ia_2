# ------------------------------------------------------
# -------------------- points_input.py --------------------
# ------------------------------------------------------
import sys
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pylab as plt
# from matplotlib.figure import Figure
import numpy as np
from collections import deque
import matplotlib.animation as animation
from matplotlib.ticker import FuncFormatter

    
class Points_Input(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        

        # Creating de graph
        self.fig = plt.figure(2)
        self.ax = plt.subplot()
        self.canvas = FigureCanvas(self.fig)  
        self.canvas.setFocus()
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.layout.addWidget(self.canvas) 
         
        self.init_graph()

        self.classes = []
        self.selected_class = []
        self.points = {}
        
        self.canvas.draw()
    
    def onclick(self, event):
        plt.figure(2)
        if self.selected_class:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c=self.selected_class[1])
            
            if self.selected_class[0] in self.points.keys():
                self.points.get(self.selected_class[0]).append([event.xdata, event.ydata])
            else:
                self.points[self.selected_class[0]] = [[event.xdata, event.ydata]]

        self.canvas.draw()

    def update_scatter_colors(self):
        plt.figure(2)
        self.clearPlot()
        for _class in self.points.items():
            points = _class[1]
            for point in points:
                plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

        self.canvas.draw()

    def init_graph(self):
        plt.figure(2)
        plt.tight_layout()
        self.ax = plt.gca()
        self.fig.set_facecolor('#323232')
        self.ax.grid(zorder=0)
        self.ax.set_axisbelow(True)
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        self.ax.set_xticks(range(-5,6))
        self.ax.set_yticks(range(-5,6))
        self.ax.axhline(y=0, color='#323232')
        self.ax.axvline(x=0, color='#323232')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.tick_params(axis='x', colors='#b1b1b1')
        self.ax.tick_params(axis='y', colors='#b1b1b1')

    def clearPlot(self):
        plt.figure(2)
        plt.clf()
        self.init_graph()
        self.canvas.draw()

    def set_donut(self):
        self.selected_class.clear()
        self.points.clear()
        self.clearPlot()

        SIZE = 10

        class_a = np.linspace(2.5,4.5,8)
        class_b = np.linspace(1.5,2,4)
        class_c = np.linspace(.2,1,5)

        theta = np.linspace(0, 2*np.pi, 60)
        for rad in class_a:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[0][1])           
                if self.classes[0][0] in self.points.keys():
                    self.points.get(self.classes[0][0]).append([x1, x2])
                else:
                    self.points[self.classes[0][0]] = [[x1, x2]]
        theta = np.linspace(0, 2*np.pi, 30)
        for rad in class_b:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[1][1])
                if self.classes[1][0] in self.points.keys():
                    self.points.get(self.classes[1][0]).append([x1, x2])
                else:
                    self.points[self.classes[1][0]] = [[x1, x2]]
        theta = np.linspace(0, 2*np.pi, 10)
        for rad in class_c:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[2][1])
                if self.classes[2][0] in self.points.keys():
                    self.points.get(self.classes[2][0]).append([x1, x2])
                else:
                    self.points[self.classes[2][0]] = [[x1, x2]]
        self.canvas.draw()