from UI.Interface_MLP import QtWidgets, Ui_MainWindow
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)