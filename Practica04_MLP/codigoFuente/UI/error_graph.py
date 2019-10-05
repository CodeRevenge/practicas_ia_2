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

    
class Error_Graph(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.fig = Figure(figsize=(1,1), dpi=10)
        _ = self.fig.add_subplot(111)
        
        self.linea = []
    
    def cargarGrafica(self, maximo, x_data = np.linspace(0,60,60+1)[0:-1], y_data = np.linspace(0,0,60+1)[0:-1], line = [], ticks = True):
        self.linea = line
        if self.linea == []:  
            fig, ax = plt.subplots()
            if ticks:
                ax.set_xticks([]) 
                ax.set_yticks([]) 
            plt.ylim(0,maximo)
            self.linea, = ax.plot(x_data,y_data,'',alpha=0.8)
            self.canvas = FigureCanvas(fig)    
            self.layout.addWidget(self.canvas)
            self.linea.set_ydata(y_data)
            self.canvas.draw()
        else:
            plt.ylim(0,maximo)
            self.linea.set_ydata(y_data)
            self.canvas.draw()
        return self.linea
 