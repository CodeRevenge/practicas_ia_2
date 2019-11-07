# ------------------------------------------------------
# -------------------- points_input.py --------------------
# ------------------------------------------------------
import sys
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pylab as plt
import numpy as np

    
class Points_Input(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.TRAIN_BUTTON = QWidget
        self.update_last_layer_input = lambda x:x
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

        self.points = []

        self.trained = False
        
        self.canvas.draw()
    
    def onclick(self, event):
        plt.figure(2)

        # if self.maped:
        #     class_output = self.algorithm.forwardPropagation([event.xdata, event.ydata])
        #     class_type = self.class_type(list(class_output))
        #     self.ax.scatter(event.xdata, event.ydata, s=10, c=self.classes[class_type][1], marker='o')
        # elif self.selected_class:
        #     plt.scatter(event.xdata, event.ydata, s=10, marker='o', c=self.selected_class[1])
            
        #     if self.selected_class[0] in self.points.keys():
        #         self.points.get(self.selected_class[0]).append([event.xdata, event.ydata])
        #     else:
        #         self.points[self.selected_class[0]] = [[event.xdata, event.ydata]]
        #         classes = len(self.points.keys())
        #         if classes > 2:
        #             try:
        #                 self.update_last_layer_input(classes)
        #             except AttributeError:
        #                 pass
        if not self.trained:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c='b')
            self.points.append([event.xdata, event.ydata])
        else:
            pass

        self.canvas.draw()

        if len(self.points) >= 2:
            self.TRAIN_BUTTON.setEnabled(True)


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
        self.maped = False
        plt.figure(2)
        plt.clf()
        self.init_graph()
        self.canvas.draw()

    

    def plot_lines(self, X = [], y = [], y_pred = []):
        self.maped = False

        x_y = np.column_stack((X,y))
        x_y_pred = np.column_stack((X,y_pred))

        x_y = x_y[x_y[:,0].argsort()]

        x_y_pred = x_y_pred[x_y_pred[:,0].argsort()]

        self.figure = plt.figure(2)
        plt.clf()
        self.init_graph()
        self.ax = plt.gca()

        self.ax.plot(x_y[:,0], x_y[:,1], '-o', label='Patrones de entrenamiento')
        self.ax.plot(x_y_pred[:,0], x_y_pred[:,1], '-o', label='Salida de la red')

        # self.ax.plot(X,y, '-o', label='Patrones de entrenamiento')
        # self.ax.plot(X, y_pred, '-o', label='Salida de la red')
        self.ax.legend()

        self.canvas.draw()
        self.maped = True





        