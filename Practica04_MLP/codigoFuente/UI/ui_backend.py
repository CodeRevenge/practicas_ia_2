from UI.Interface_MLP import QtWidgets, Ui_MainWindow, QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QHBoxLayout, QColorDialog
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
from matplotlib import colors as mcolors





class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        self.setupUi(self)

        self.btn_clean_input_graph.clicked.connect(self.input_graph.clearPlot)
        self.btn_generate_classes.clicked.connect(self.generate_classes)

        self.classes_layout = QHBoxLayout()
        self.classes_area.setLayout(self.classes_layout)

        self.generate_classes()

        self.selected_class = []


    def generate_classes(self):
        for i in reversed(range(self.classes_layout.count())): 
            self.classes_layout.itemAt(i).widget().deleteLater()

        for i in range(1, int(self.classes_cout.value())+1):
            self.classes_layout.addWidget(self.class_button(i, np.random.choice(list(self.colors.values()))))

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
        return False

    def pick_color(self, button):
        color = QColorDialog.getColor()
        button.setStyleSheet('QPushButton{background-color:'+ color.name() +'}QPushButton:focus{	border: 3px solid rgb(255, 85, 0);}')