from UI.Interface_MLP import QtWidgets, Ui_MainWindow, QtCore
from PyQt5.QtCore import QEvent, Qt, QThread
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QColorDialog, QSpinBox,QWidget
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
from matplotlib import colors as mcolors
import threading
from Algorithms.MultiLayerAdaline import MLP
import Algorithms.ann as ANN

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.clear_points)
        self.btn_generate_classes.clicked.connect(self.generate_classes)
        self.btn_generate_layers.clicked.connect(self.generate_layers)
        self.btn_donut.clicked.connect(self.set_donut)
        self.btn_map.clicked.connect(self.set_map)
        self.btn_xor.clicked.connect(self.set_xor)
        self.btn_plot_lines.clicked.connect(self.get_lines)
        self.btn_train.clicked.connect(self.train_mlp)
        self.btn_plot_lines.clicked.connect(self.show_lines)
        self.btn_plot_planes.clicked.connect(self.show_planes)

        self.classes_layout = QHBoxLayout()
        self.classes_area.setLayout(self.classes_layout)
        self.layers_layout = QHBoxLayout()
        self.layers_area.setLayout(self.layers_layout)

        self.generate_classes()
        self.generate_layers()

        self.input_graph.onclick

        self.temp_error = []

        self.input_graph.TRAIN_BUTTON = self.btn_train

    def generate_layers(self):
        for i in reversed(range(self.layers_layout.count())): 
            self.layers_layout.itemAt(i).widget().deleteLater()

        for i in range(1, int(self.layer_count.value())+1):
            if i == int(self.layer_count.value()):
                self.layers_layout.addWidget(self.layer_widget(i,int(self.classes_cout.value())))
            else:
                self.layers_layout.addWidget(self.layer_widget(i))            

    def generate_classes(self):
        self.clear_points()
        self.input_graph.classes.clear()
        for i in reversed(range(self.classes_layout.count())): 
            self.classes_layout.itemAt(i).widget().deleteLater()

        for i in range(1, int(self.classes_cout.value())+1):
            button = self.class_button(i, np.random.choice(list(self.colors.values())))
            self.classes_layout.addWidget(button)
            self.input_graph.classes.append([button.objectName()[-1], button.palette().color(QtGui.QPalette.Background).name()])

        self.btn_train.setEnabled(False)
        self.generate_layers()
        self.error_graph.clear_graph()

    def class_button(self, index, color):
        button = QPushButton("Clase #{}".format(index))
        button.setFixedWidth(70)
        button.setFixedHeight(50)
        button.setObjectName("btn_class_"+str(index))
        button.installEventFilter(self)
        if type(color) is tuple:
            button.setStyleSheet('QPushButton{background-color: rgb'+str(color)+';}QPushButton:focus{	border: 3px solid rgb(255, 85, 0);}')
        else:
            button.setStyleSheet('QPushButton{background-color:'+color+'}QPushButton:focus{	border: 3px solid rgb(255, 85, 0);}')
        return button

    def eventFilter(self, QObject, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton:
                self.pick_color(QObject)
            elif event.button() == Qt.LeftButton:
                self.select_class(QObject)
        return False

    def select_class(self, QObject):
        color = QObject.palette().color(QtGui.QPalette.Background).name()
        class_index = QObject.objectName()[-1]
        self.input_graph.selected_class = [class_index, color]

    def pick_color(self, button):
        color = QColorDialog.getColor()
        button.setStyleSheet('QPushButton{background-color:'+ color.name() +'}QPushButton:focus{	border: 3px solid rgb(255, 85, 0);}')
        self.input_graph.selected_class = [button.objectName()[-1], button.palette().color(QtGui.QPalette.Background).name()]
        self.input_graph.classes[int(button.objectName()[-1])-1] = [button.objectName()[-1], button.palette().color(QtGui.QPalette.Background).name()]
        self.input_graph.update_scatter_colors()

    def layer_widget(self, index, value = 2):
        widget = QWidget()
        widget.setFixedHeight(51)
        widget.setFixedWidth(71)
        widget.setObjectName("inp_layer_" + str(index))
        
        label = QtWidgets.QLabel(widget)
        label.setGeometry(QtCore.QRect(0, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label_layer_" + str(index))
        label.setText("Capa #" + str(index))

        input_spin = QSpinBox(widget)
        input_spin.setMaximum(10)
        input_spin.setMinimum(1)
        input_spin.setGeometry(QtCore.QRect(0, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        input_spin.setFont(font)
        input_spin.setFrame(True)
        input_spin.setAlignment(QtCore.Qt.AlignCenter)
        input_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        input_spin.setKeyboardTracking(True)
        input_spin.setMaximum(100)
        input_spin.setMinimum(1)
        if index == 1:
            input_spin.setProperty("value", 2)
            input_spin.lineEdit().setReadOnly(True)
        else:
            input_spin.setProperty("value", value)
        if value > 2:
            input_spin.lineEdit().setReadOnly(True)
        input_spin.setObjectName("neuron_layer_" + str(index))
        input_spin.setStyleSheet("QSpinBox { border: 1px solid #b1b1b1; background-color: #323232; border-radius: 5px;} QSpinBox:focus{ border: 2px solid #ffaa00;background-color: #4d4d4d;}QSpinBox:!focus:hover{ border: 1px solid #7e7e7e;}")

        return widget

    def clear_points(self):
        self.disable_show_btn()
        self.input_graph.clearPlot()
        self.input_graph.points.clear()
        self.input_graph.selected_class.clear()
        self.error_graph.clear_graph()
        self.btn_train.setEnabled(False)

    def set_donut(self):
        self.disable_show_btn()
        self.input_graph.set_donut()
        self.activate_train()
        self.error_graph.clear_graph()
    
    def set_map(self):
        self.disable_show_btn()
        if self.classes_cout.value() != 5:
            self.classes_cout.setValue(5)
            self.generate_classes()
        self.input_graph.set_map()
        self.activate_train()
        self.error_graph.clear_graph()

    def set_xor(self):
        self.disable_show_btn()
        self.input_graph.set_xor()
        self.activate_train()
        self.error_graph.clear_graph()

    def validate_activation(self):
        print("OK")
        if len(self.input_graph.points.keys()) >= 3:
            self.activate_train()

    def activate_train(self):
        self.btn_train.setEnabled(True)
    
    def convert_dict_to_inputs(self, dictionary):
        self._inputs = []
        self._targets = []
        for key in list(dictionary):
            for point in dictionary[key]:
                self._inputs.append([point[0],point[1]])
                highest_class = int(max(list(dictionary)))
                target = np.zeros(highest_class, dtype=np.int32)
                target[int(key)-1]=1
                self._targets.append(list(target))

    def get_architecture(self):
        architecture = []
        for i in range(self.layers_layout.count()): 
            architecture.append(int(self.layers_layout.itemAt(i).widget().findChildren(QSpinBox)[0].value()))
        return architecture

    def get_lines(self):
        pass

    def train_mlp(self):
        self.disable_show_btn()
        # Integer with the count of classes
        self._classes_count = len(self.input_graph.points.keys())
        # List of Lists with all the inputs with the form [[x,y,class],...]
        self.convert_dict_to_inputs(self.input_graph.points)
        # List of Integers with the architecture with the form [layer_1_count, layer_2_count, ...]
        self._architecture = self.get_architecture()
        self._architecture.pop(0)
        # Integer with the learning rate
        self._learning_rate = float(self.learning_rate.value())
        # Integer with the min error
        self._min_error = float(self.min_error.value())
        # Integer with the count of max ephocs
        self._max_ephocs = int(self.max_ephocs.value())
        
        self.disable_all()
        self.progressBar.setValue(0)
        
        # print("Classes count: {} \nArchitecture: {} \nLearning rate: {} \nMin error: {} \nMax ephocs: {}".format(self._classes_count, self._architecture, self._learning_rate, self._min_error, self._max_ephocs))

        """ Here is where the MLP must be instantiated"""
        self.hilo = threading.Thread(target=self.ejecute_algorithm)
        self.hilo.start()

    def ejecute_algorithm(self):
        self.ann = ANN.NeuralNetwork(layers_structure= self._architecture, bias= [0.35], learning_rate= self._learning_rate)
        self.train = ANN.TRAIN(all_inputs= self._inputs, all_targets= self._targets, min_error= self._min_error, max_epochs= self._max_ephocs, NN=self.ann)
        self.train.countChanged.connect(self.onCountChanged)
        self.train.finished.connect(self.onFinished)
        self.train.start()

    def onCountChanged(self, value):
        self.progressBar.setValue(value)

    def onFinished(self):
        self.progressBar.setValue(80)
        self.input_graph.fill_plot(self.ann, self.progressBar)
        self.error_graph.graph_errors(self.train.errors)
        self.btn_plot_lines.setEnabled(True)
        self.enable_all()

    def show_lines(self):
        self.input_graph.show_lines(self.ann.hidden_layers[0].neurons)
        self.btn_plot_planes.setEnabled(True)
        self.btn_plot_lines.setEnabled(False)

    def show_planes(self):
        self.input_graph.show_planes()
        self.btn_plot_planes.setEnabled(False)
        self.btn_plot_lines.setEnabled(True)

    def disable_show_btn(self):
        self.btn_plot_planes.setEnabled(False)
        self.btn_plot_lines.setEnabled(False)

    def disable_all(self):
        self.btn_clean_input_graph.setEnabled(False)
        self.btn_generate_classes.setEnabled(False)
        self.btn_generate_layers.setEnabled(False)
        self.btn_donut.setEnabled(False)
        self.btn_map.setEnabled(False)
        self.btn_xor.setEnabled(False)
        self.btn_train.setEnabled(False)
        self.btn_plot_lines.setEnabled(False)
        self.btn_plot_planes.setEnabled(False)
        self.input_graph.setEnabled(False)

    def enable_all(self):
        self.btn_clean_input_graph.setEnabled(True)
        self.btn_generate_classes.setEnabled(True)
        self.btn_generate_layers.setEnabled(True)
        self.btn_donut.setEnabled(True)
        self.btn_map.setEnabled(True)
        self.btn_xor.setEnabled(True)
        self.btn_train.setEnabled(True)
        self.btn_plot_lines.setEnabled(True)
        self.input_graph.setEnabled(True)
    