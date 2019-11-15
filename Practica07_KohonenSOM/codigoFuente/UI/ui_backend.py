from UI.Interface_RBF import QtWidgets, Ui_MainWindow, QtCore
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
from Algorithms.RBF import RBF

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.clear_points)
        self.btn_train.clicked.connect(self.train_rbf)

        self.input_graph.onclick

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

        #
        # NUM_SAMPLES = 100
        # X = np.random.uniform(0, 5, NUM_SAMPLES)
        # X = np.sort(X, axis=0)
        # noise = np.random.uniform(-0.2, 0.2, NUM_SAMPLES)
        # y = np.sin(2 * np.pi * X)*2  + noise + 2

        # self.train = RBF(self._hidden_neurons, self._learning_rate, self._max_ephocs, self._min_error)
        # self.train.fit(X, y)
        
        # y_pred = self.train.predict(X)
        # self.input_graph.plot_lines(X, y, y_pred)
        #


        self.train = RBF(self._hidden_neurons, self._learning_rate, self._max_ephocs, self._min_error)
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
    