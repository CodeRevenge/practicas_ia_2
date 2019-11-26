# ------------------------------------------------------
# -------------------- points_input.py --------------------
# ------------------------------------------------------
import sys
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pylab as plt
from matplotlib import patches as patches
import numpy as np

    
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
        self.layout.addWidget(self.canvas) 
         
        self.init_graph()
        self.canvas.draw()


    def init_graph(self):
        plt.figure(2)
        plt.tight_layout()
        self.ax = plt.gca()
        self.fig.set_facecolor('#323232')
        self.ax.grid(zorder=0)
        self.ax.set_axisbelow(True)
        self.ax.set_xlim([0, 5])
        self.ax.set_ylim([0, 5])
        self.ax.set_xticks(range(0,6))
        self.ax.set_yticks(range(0,6))
        self.ax.axhline(y=0, color='#323232')
        self.ax.axvline(x=0, color='#323232')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.tick_params(axis='x', colors='#b1b1b1')
        self.ax.tick_params(axis='y', colors='#b1b1b1')

    def clearPlot(self):
        self.fig = plt.figure(2)
        self.fig.clf()
        self.ax = plt.gca()
        self.ax.cla()
        # self.init_graph()
        self.canvas.draw()

    

    def plot_lines(self, net):
        self.clearPlot()
        self.fig = plt.figure(2)
        self.ax = plt.gca()
        self.fig.set_facecolor('#323232')
        # setup axes
        # self.ax = self.fig.add_subplot(111, aspect='equal')
        self.ax.set_xlim((0, net.shape[0]+1))
        self.ax.set_ylim((0, net.shape[1]+1))
        self.ax.tick_params(axis='x', colors='#b1b1b1')
        self.ax.tick_params(axis='y', colors='#b1b1b1')

        # plot the rectangles
        for x in range(1, net.shape[0] + 1):
            for y in range(1, net.shape[1] + 1):
                face_color = net[x-1,y-1,:]
                face_color = [sum(face_color[:3])/3,sum(face_color[3:6])/3, sum(face_color[6:])/4]
                self.ax.add_patch(patches.Rectangle((x-0.5, y-0.5), 1, 1,
                            #  facecolor=net[x-1,y-1,:],
                            facecolor=face_color,
                            edgecolor='none'))
        self.canvas.draw()





        