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
        self.maped = False
        plt.figure(2)
        plt.clf()
        self.init_graph()
        self.canvas.draw()

    

    # def fill_plot(self, algorithm, progress_bar, size = 30, dpi = 40):
    #     self.maped = False
    #     self.algorithm = algorithm

    #     self.figure = plt.figure(2)
    #     plt.clf()
    #     self.init_graph()
    #     self.ax = plt.gca()
    #     self.colors_class_type(len(self.classes))

    #     progress = 20 / dpi
    #     progress_count = 80

    #     x = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
    #     y = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
    #     self.plane.clear()

    #     for ind, i in enumerate(y):
    #         self.plane.append([])
    #         for j in x:
    #             class_output = self.algorithm.forwardPropagation([j,i])
    #             class_type = self.class_type(list(class_output))
    #             self.plane[ind].append(class_type)
    #             self.ax.scatter(j, i, s=size, c=self.colors_class[class_type], marker='s')
    #         progress_count += progress
    #         progress_bar.setValue(progress_count)

    #     for _class in self.points.items():
    #         points = _class[1]
    #         for point in points:
    #             plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

    #     self.canvas.draw()
    #     self.maped = True

    # def normalize_class(self, class_vector):
    #     normalized_class = list(np.zeros(len(class_vector),dtype=np.int32))
    #     normalized_class[class_vector.index(max(class_vector))] = 1
    #     return normalized_class

    # def class_type(self, class_vector):
    #     return class_vector.index(max(class_vector))

    # def colors_class_type(self, classes_count):
    #     colors = ['red', 'black', 'darkgreen', 'navy', 'orange', 'yellowgreen', 'fuchsia', 'gold', 'cyan', 'pink', 'brown']
    #     self.colors_class = []
    #     for _ in range(classes_count):
    #         color = np.random.choice(colors)
    #         colors.pop(colors.index(color))
    #         self.colors_class.append(color)


    # def show_lines(self, init_layer, bias):
    
    #     plt.figure(2)
    #     plt.clf()
    #     plt.tight_layout()

    #     self.fig = plt.figure(2)
    #     self.ax = plt.gca()
    #     self.init_lines(self.fig, self.ax)

    #     for index, (neuron, tetha) in enumerate(zip(init_layer,bias)):
    #         w1 = neuron[0]
    #         w2 = neuron[1]
    #         y = [(-(tetha/w1)/(tetha/w2))*-5+(-tetha/w1),(-(tetha/w1)/(tetha/w2))*5+(-tetha/w1)]
    #         x = [-5,5]
    #         line, = self.ax.plot(x,y)
    #         line.set_label('Neurona {}'.format(index+1))
        
    #     self.ax.legend()

    #     for _class in self.points.items():
    #         points = _class[1]
    #         for point in points:
    #             self.ax.scatter(point[0], point[1], s=5, marker='o', c=self.classes[int(_class[0])-1][1])


    #     self.canvas.draw()

    # def show_planes(self, size = 30, dpi = 40):
    #     self.figure = plt.figure(2)
    #     plt.clf()
    #     self.init_graph()
    #     self.ax = plt.gca()

    #     x = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
    #     y = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))

    #     for ind_y, i in enumerate(y):
    #         for ind_x, j in enumerate(x):
    #             class_type = self.plane[ind_y][ind_x]
    #             self.ax.scatter(j, i, s=size, c=self.colors_class[class_type], marker='s')

    #     for _class in self.points.items():
    #         points = _class[1]
    #         for point in points:
    #             plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

    #     self.canvas.draw()

    # def init_lines(self, fig, ax):
    #     fig.set_facecolor('#323232')
    #     ax.grid(zorder=0)
    #     ax.set_axisbelow(True)
    #     ax.set_xlim([-5, 5])
    #     ax.set_ylim([-5, 5])
    #     ax.set_xticks(range(-5,6))
    #     ax.set_yticks(range(-5,6))
    #     ax.axhline(y=0, color='#323232')
    #     ax.axvline(x=0, color='#323232')
    #     ax.spines['right'].set_visible(False)
    #     ax.spines['top'].set_visible(False)
    #     ax.spines['bottom'].set_visible(False)
    #     ax.spines['left'].set_visible(False)
    #     ax.tick_params(axis='x', colors='#b1b1b1')
    #     ax.tick_params(axis='y', colors='#b1b1b1')




        