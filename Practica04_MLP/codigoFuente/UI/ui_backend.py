from UI.Interface_MLP import QtWidgets, Ui_MainWindow, QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QColorDialog, QSpinBox,QWidget
from PyQt5 import QtGui
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
from matplotlib import colors as mcolors

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.clear_points)
        self.btn_generate_classes.clicked.connect(self.generate_classes)
        self.btn_generate_layers.clicked.connect(self.generate_layers)
        self.btn_donut.clicked.connect(self.set_donut)

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

    def layer_widget(self, index, value = 1):
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
        input_spin.setProperty("value", value)
        input_spin.setObjectName("neuron_layer_" + str(index))
        input_spin.setStyleSheet("QSpinBox { border: 1px solid #b1b1b1; background-color: #323232; border-radius: 5px;} QSpinBox:focus{ border: 2px solid #ffaa00;background-color: #4d4d4d;}QSpinBox:!focus:hover{ border: 1px solid #7e7e7e;}")

        return widget

    def clear_points(self):
        self.input_graph.clearPlot()
        self.input_graph.points.clear()
        self.input_graph.selected_class.clear()
        self.btn_train.setEnabled(False)

    def set_donut(self):
        self.input_graph.set_donut()
        self.activate_train()

    def validate_activation(self):
        print("OK")
        if len(self.input_graph.points.keys()) >= 3:
            self.activate_train()

    def activate_train(self):
        self.btn_train.setEnabled(True)

    def train_mlp(self):
        pass