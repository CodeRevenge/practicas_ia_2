from UI.Interface_SOM import QtWidgets, Ui_MainWindow, QtCore
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
import threading
from Algorithms.SOM import SOM

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.clear_points)
        self.btn_train.clicked.connect(self.train_som)

    def clear_points(self):
        self.input_graph.clearPlot()
        self.input_graph.points.clear()
        self.error_graph.clear_graph()
        self.btn_train.setEnabled(False)


    def train_som(self):
        # String with the Neighborhood type
        self.k_neighborhood = str(self.cbx_neighborhood.currentText())
        # String with the distance function
        self.k_distance = str(self.cbx_distance.currentText())
        # Integer with the size of the grid
        self.mesh_size = int(self.inp_grid_size.value())
        # Integer with the count of max ephocs
        self.max_ephocs = int(self.inp_ephocs.value())
        # Double with the learning rate
        self.learning_rate = float(self.inp_learning_rate.value())
        
        self.btn_train.setEnabled(False)

        self.som = SOM(self.k_neighborhood, self.k_distance, self.mesh_size, self.max_ephocs, self.learning_rate)
        self.som.countChanged.connect(self.onCountChanged)
        self.som.finished.connect(self.onFinished)
        self.som.start()

    def onCountChanged(self, value):
        self.progressBar.setValue(value)

    def onFinished(self):
        print('finished')
        self.progressBar.setValue(100)
        self.input_graph.plot_lines(self.som.net)
        self.btn_train.setEnabled(True)