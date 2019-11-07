from UI.Interface_RBF import QtWidgets, Ui_MainWindow, QtCore
from PyQt5.QtCore import QEvent, Qt, QThread
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QColorDialog, QSpinBox,QWidget
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
from matplotlib import colors as mcolors
import threading
from Algorithms.RBFnet import RBFNet

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.clear_points)
        self.btn_train.clicked.connect(self.train_rbf)

        self.input_graph.onclick

        self.temp_error = []

        self.input_graph.TRAIN_BUTTON = self.btn_train

    def clear_points(self):
        self.input_graph.clearPlot()
        self.input_graph.points.clear()
        self.error_graph.clear_graph()
        self.btn_train.setEnabled(False)


    def train_rbf(self):
        # List of with all the inputs with the form [x1,x2,...,xn]
        self._points = np.array(self.input_graph.points)
        # Tuple of Integers with the architecture with the form [layer_1_count, layer_2_count, ...]
        self._hidden_neurons = int(self.hidden_layer_count.value())
        # Integer with the learning rate
        self._learning_rate = float(self.learning_rate.value())
        # Integer with the min error
        self._min_error = float(self.min_error.value())
        # Integer with the count of max ephocs
        self._max_ephocs = int(self.max_ephocs.value())
        
        self.disable_all()
        self.train = RBFNet(self._hidden_neurons, self._learning_rate, self._max_ephocs)
        self.train.fit(self._points[:,0], self._points[:,1])

        self.y_predic = self.train.predict(self._points[:,0])

        self.input_graph.plot_lines(self._points[:,0], self._points[:,1], self.y_predic)



        self.error_graph.graph_errors(self.train.errors)
        self.enable_all()


    def disable_all(self):
        self.btn_clean_input_graph.setEnabled(False)
        self.btn_train.setEnabled(False)
        self.input_graph.setEnabled(False)

    def enable_all(self):
        self.btn_clean_input_graph.setEnabled(True)
        self.btn_train.setEnabled(True)
        self.input_graph.setEnabled(True)
    