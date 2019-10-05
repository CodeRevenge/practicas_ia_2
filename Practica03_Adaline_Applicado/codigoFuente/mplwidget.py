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

    
class MplWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.fig = Figure(figsize=(1,1), dpi=10)
        _ = self.fig.add_subplot(111)
        self.linea = []


    def cargarGrafico(self, x_data, y_data):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
        self.linea, = ax.plot(x_data,y_data,'',alpha=0.8)
        self.canvas = FigureCanvas(fig)    
        self.layout.addWidget(self.canvas)
        self.canvas.draw()

    def cargarGraficoDinamico(self, x_data, y_data, epocas_max, linea):
        self.linea = linea
        if self.linea == []:  
            for i in reversed(range(self.layout.count())): 
                self.layout.itemAt(i).widget().setParent(None)
            plt.xlim(0,epocas_max)
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
            self.linea, = ax.plot(x_data,y_data,'',alpha=0.8)
            self.canvas = FigureCanvas(fig)    
            self.layout.addWidget(self.canvas)
            self.canvas.draw()
        else:
            self.linea.set_ydata(y_data)
            self.linea.set_xdata(x_data)
            self.canvas.draw()
        return self.linea
        
