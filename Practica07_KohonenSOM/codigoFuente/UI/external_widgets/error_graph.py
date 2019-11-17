# ------------------------------------------------------
# -------------------- error_graph.py --------------------
# ------------------------------------------------------
import sys
from collections import deque

import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter
from PyQt5.QtWidgets import QVBoxLayout, QWidget
import time


class Error_Graph(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # self.layout.setContentsMargins(0,0,0,0)

        self.TITLE_STYLE = {
            'size': 12,
            'color': "#b1b1b1"
        }

        # Creating de graph
        self.figure = plt.figure(1)
        self.ax = plt.subplot()
        self.canvas = FigureCanvas(self.figure) 
        self.canvas.setFocus()
        self.layout.addWidget(self.canvas) 

        self.error_points = []
        self.min_error_reached = int
        self.max_ephocs_reached = int
        
        self.init_graph()
        self.canvas.draw()
    

    def init_graph(self, x_max = 2000, y_max = 15):
        self.figure = plt.figure(1)
        self.figure.clf()
        self.figure.tight_layout()
        self.ax = self.figure.gca()
        self.figure.set_facecolor('#323232')
        self.ax.grid(zorder=0)
        self.ax.set_axisbelow(True)
        self.ax.set_xlim([0, x_max])
        self.ax.set_ylim([0, y_max])
        self.ax.set_yticks((0,(y_max)/2, y_max))
        self.ax.axhline(y=0, color='#323232')
        self.ax.axvline(x=0, color='#323232')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.tick_params(axis='x', colors='#b1b1b1')
        self.ax.tick_params(axis='y', colors='#b1b1b1')

    def clear_plot(self):
        plt.figure(1)
        self.ax = plt.gca()
        self.ax.cla()
        self.init_graph()
        self.canvas.draw()

    def set_title(self, min_error = '', max_ephocs = ''):
        plt.figure(1)
        self.ax = plt.gca()
        self.ax.set_title('Error mínimo alcanzado: {:.6f}'.format(min_error), fontdict = self.TITLE_STYLE)

    def add_error(self, error):
        plt.figure(1)
        self.ax = plt.gca()
        self.ax.cla()
        self.ax.grid(zorder=0)
        self.error_points.append(error)
        self.ax.plot(self.error_points)
        self.set_title(error, len(self.error_points))
        self.canvas.draw()


    def clear_graph(self):
        plt.figure(1)
        plt.clf()
        self.init_graph()
        self.canvas.draw()
        np.sqrt()
    

    def graph_errors(self, errors):
        if type(errors) == np.ndarray:
            self.error_points = errors.copy()
        else:
            self.error_points = list.copy(errors)
        # self.figure = plt.figure(1)
        # self.figure.clf()
        # self.figure.tight_layout()
        # self.ax = self.figure.gca()
        # self.ax.cla()
        # self.ax.grid(zorder=0)
        self.init_graph(len(self.error_points), max(self.error_points))
        self.ax.plot(self.error_points, c='red')
        try:
            self.set_title(self.error_points[-1], len(self.error_points))
        except IndexError:
            self.set_title(0, len(self.error_points))

        self.canvas.draw()