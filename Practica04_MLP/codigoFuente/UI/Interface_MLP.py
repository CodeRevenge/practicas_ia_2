# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Interface_MLP.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1271, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/inteligencia-artificial.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QDoubleSpinBox, QSpinBox\n"
"{\n"
"    border: 1px solid #b1b1b1;\n"
"    background-color: #323232;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus , QSpinBox:focus\n"
"{\n"
"    border: 2px solid #ffaa00;\n"
"    background-color: #4d4d4d;\n"
"}\n"
"\n"
"QDoubleSpinBox:!focus:hover , QSpinBox:!focus:hover\n"
"{\n"
"    border: 1px solid #7e7e7e;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    color:rgb(98, 98, 98);\n"
"    border-radius:5px;\n"
"    border: 1px solid rgb(65, 65, 65);\n"
"    background-color: rgb(66, 66, 66);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(10, 10, 681, 441))
        self.input_box.setObjectName("input_box")
        self.input_graph = Points_Input(self.input_box)
        self.input_graph.setGeometry(QtCore.QRect(10, 20, 661, 381))
        self.input_graph.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_graph.setStyleSheet("padding: 0px;")
        self.input_graph.setObjectName("input_graph")
        self.btn_clean_input_graph = QtWidgets.QPushButton(self.input_box)
        self.btn_clean_input_graph.setGeometry(QtCore.QRect(260, 400, 151, 31))
        self.btn_clean_input_graph.setObjectName("btn_clean_input_graph")
        self.error_box = QtWidgets.QGroupBox(self.centralwidget)
        self.error_box.setGeometry(QtCore.QRect(10, 460, 681, 191))
        self.error_box.setObjectName("error_box")
        self.error_graph = Error_Graph(self.error_box)
        self.error_graph.setGeometry(QtCore.QRect(10, 15, 661, 170))
        self.error_graph.setObjectName("error_graph")
        self.control_box = QtWidgets.QGroupBox(self.centralwidget)
        self.control_box.setGeometry(QtCore.QRect(710, 10, 551, 641))
        self.control_box.setObjectName("control_box")
        self.label = QtWidgets.QLabel(self.control_box)
        self.label.setGeometry(QtCore.QRect(10, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.learning_rate = QtWidgets.QDoubleSpinBox(self.control_box)
        self.learning_rate.setGeometry(QtCore.QRect(300, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.learning_rate.setFont(font)
        self.learning_rate.setStyleSheet("")
        self.learning_rate.setFrame(True)
        self.learning_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.learning_rate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.learning_rate.setKeyboardTracking(True)
        self.learning_rate.setPrefix("")
        self.learning_rate.setDecimals(3)
        self.learning_rate.setMinimum(0.001)
        self.learning_rate.setMaximum(0.999)
        self.learning_rate.setSingleStep(0.01)
        self.learning_rate.setProperty("value", 0.5)
        self.learning_rate.setObjectName("learning_rate")
        self.min_error = QtWidgets.QDoubleSpinBox(self.control_box)
        self.min_error.setGeometry(QtCore.QRect(300, 70, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_error.setFont(font)
        self.min_error.setFrame(True)
        self.min_error.setAlignment(QtCore.Qt.AlignCenter)
        self.min_error.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_error.setKeyboardTracking(True)
        self.min_error.setPrefix("")
        self.min_error.setDecimals(6)
        self.min_error.setMinimum(1e-06)
        self.min_error.setMaximum(0.999999)
        self.min_error.setSingleStep(0.01)
        self.min_error.setProperty("value", 0.02)
        self.min_error.setObjectName("min_error")
        self.label_2 = QtWidgets.QLabel(self.control_box)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.max_ephocs = QtWidgets.QSpinBox(self.control_box)
        self.max_ephocs.setGeometry(QtCore.QRect(300, 120, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_ephocs.setFont(font)
        self.max_ephocs.setFrame(True)
        self.max_ephocs.setAlignment(QtCore.Qt.AlignCenter)
        self.max_ephocs.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.max_ephocs.setKeyboardTracking(True)
        self.max_ephocs.setMinimum(1)
        self.max_ephocs.setMaximum(999999999)
        self.max_ephocs.setProperty("value", 2000)
        self.max_ephocs.setObjectName("max_ephocs")
        self.label_3 = QtWidgets.QLabel(self.control_box)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.control_box)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.classes_cout = QtWidgets.QSpinBox(self.control_box)
        self.classes_cout.setGeometry(QtCore.QRect(10, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.classes_cout.setFont(font)
        self.classes_cout.setFrame(True)
        self.classes_cout.setAlignment(QtCore.Qt.AlignCenter)
        self.classes_cout.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.classes_cout.setKeyboardTracking(True)
        self.classes_cout.setMinimum(3)
        self.classes_cout.setMaximum(10)
        self.classes_cout.setProperty("value", 3)
        self.classes_cout.setObjectName("classes_cout")
        self.btn_generate_classes = QtWidgets.QPushButton(self.control_box)
        self.btn_generate_classes.setGeometry(QtCore.QRect(10, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_generate_classes.setFont(font)
        self.btn_generate_classes.setObjectName("btn_generate_classes")
        self.btn_train = QtWidgets.QPushButton(self.control_box)
        self.btn_train.setEnabled(False)
        self.btn_train.setGeometry(QtCore.QRect(10, 550, 531, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_train.setFont(font)
        self.btn_train.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_train.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.btn_train.setObjectName("btn_train")
        self.label_5 = QtWidgets.QLabel(self.control_box)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layer_count = QtWidgets.QSpinBox(self.control_box)
        self.layer_count.setGeometry(QtCore.QRect(10, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.layer_count.setFont(font)
        self.layer_count.setFrame(True)
        self.layer_count.setAlignment(QtCore.Qt.AlignCenter)
        self.layer_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.layer_count.setKeyboardTracking(True)
        self.layer_count.setMinimum(3)
        self.layer_count.setMaximum(10)
        self.layer_count.setProperty("value", 3)
        self.layer_count.setObjectName("layer_count")
        self.btn_generate_layers = QtWidgets.QPushButton(self.control_box)
        self.btn_generate_layers.setGeometry(QtCore.QRect(10, 390, 151, 31))
        self.btn_generate_layers.setObjectName("btn_generate_layers")
        self.neurons_box = QtWidgets.QGroupBox(self.control_box)
        self.neurons_box.setGeometry(QtCore.QRect(170, 310, 371, 111))
        self.neurons_box.setObjectName("neurons_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.neurons_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scroll_area_layers = QtWidgets.QScrollArea(self.neurons_box)
        self.scroll_area_layers.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scroll_area_layers.setStyleSheet("border: 1px solid #323232")
        self.scroll_area_layers.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_layers.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_area_layers.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scroll_area_layers.setWidgetResizable(True)
        self.scroll_area_layers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scroll_area_layers.setObjectName("scroll_area_layers")
        self.layers_area = QtWidgets.QWidget()
        self.layers_area.setGeometry(QtCore.QRect(0, 0, 349, 76))
        self.layers_area.setObjectName("layers_area")
        self.scroll_area_layers.setWidget(self.layers_area)
        self.gridLayout_2.addWidget(self.scroll_area_layers, 0, 0, 1, 1)
        self.btn_donut = QtWidgets.QPushButton(self.control_box)
        self.btn_donut.setGeometry(QtCore.QRect(10, 440, 51, 51))
        self.btn_donut.setObjectName("btn_donut")
        self.btn_x = QtWidgets.QPushButton(self.control_box)
        self.btn_x.setGeometry(QtCore.QRect(70, 440, 51, 51))
        self.btn_x.setObjectName("btn_x")
        self.btn_map = QtWidgets.QPushButton(self.control_box)
        self.btn_map.setGeometry(QtCore.QRect(130, 440, 51, 51))
        self.btn_map.setObjectName("btn_map")
        self.btn_plot_lines = QtWidgets.QPushButton(self.control_box)
        self.btn_plot_lines.setEnabled(False)
        self.btn_plot_lines.setGeometry(QtCore.QRect(210, 440, 161, 21))
        self.btn_plot_lines.setObjectName("btn_plot_lines")
        self.btn_plot_areas = QtWidgets.QPushButton(self.control_box)
        self.btn_plot_areas.setEnabled(False)
        self.btn_plot_areas.setGeometry(QtCore.QRect(210, 470, 161, 21))
        self.btn_plot_areas.setObjectName("btn_plot_areas")
        self.progressBar = QtWidgets.QProgressBar(self.control_box)
        self.progressBar.setGeometry(QtCore.QRect(10, 610, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.classes_box = QtWidgets.QGroupBox(self.control_box)
        self.classes_box.setGeometry(QtCore.QRect(170, 180, 371, 111))
        self.classes_box.setObjectName("classes_box")
        self.gridLayout = QtWidgets.QGridLayout(self.classes_box)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.classes_box)
        self.scrollArea.setStyleSheet("border: 1px solid #323232")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.classes_area = QtWidgets.QWidget()
        self.classes_area.setGeometry(QtCore.QRect(0, 0, 349, 76))
        self.classes_area.setObjectName("classes_area")
        self.scrollArea.setWidget(self.classes_area)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.label.raise_()
        self.learning_rate.raise_()
        self.min_error.raise_()
        self.label_2.raise_()
        self.max_ephocs.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.btn_generate_classes.raise_()
        self.btn_train.raise_()
        self.label_5.raise_()
        self.btn_generate_layers.raise_()
        self.neurons_box.raise_()
        self.btn_donut.raise_()
        self.btn_x.raise_()
        self.btn_map.raise_()
        self.btn_plot_lines.raise_()
        self.btn_plot_areas.raise_()
        self.progressBar.raise_()
        self.classes_box.raise_()
        self.classes_cout.raise_()
        self.layer_count.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MultiLayer Adaline"))
        self.input_box.setTitle(_translate("MainWindow", "Entrada de puntos"))
        self.btn_clean_input_graph.setText(_translate("MainWindow", "Limpiar gráfica"))
        self.error_box.setTitle(_translate("MainWindow", "Errores"))
        self.control_box.setTitle(_translate("MainWindow", "Controles"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Especifique el ratio de aprendizaje para el MLP.</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Ratio de aprendizaje:"))
        self.learning_rate.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ratio de aprendizaje entre 1 y 0.</p></body></html>"))
        self.min_error.setToolTip(_translate("MainWindow", "<html><head/><body><p>El error mínimo mientras más pequeño mejor para el entrenamiento.</p></body></html>"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el error mínimo.</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Error mínimo:"))
        self.max_ephocs.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cantidad de épocas entre 0 y 999999.</p></body></html>"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Especifique el número de épocas máximas.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Épocas máximas:"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Número de clases"))
        self.classes_cout.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 clases.</p></body></html>"))
        self.btn_generate_classes.setText(_translate("MainWindow", "Generar clases"))
        self.btn_train.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Primero debe ingresar al menos 3 puntos de diferentes clases para activar el entrenamiento del MLP.</span></p></body></html>"))
        self.btn_train.setText(_translate("MainWindow", "Entrenar MLP"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Número de capas"))
        self.layer_count.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mínimo 3 y máximo 10 capas.</p></body></html>"))
        self.btn_generate_layers.setText(_translate("MainWindow", "Generar capas"))
        self.neurons_box.setTitle(_translate("MainWindow", "Neuronas por capa"))
        self.btn_donut.setText(_translate("MainWindow", "Dona"))
        self.btn_x.setText(_translate("MainWindow", "Equis"))
        self.btn_map.setText(_translate("MainWindow", "Mapa"))
        self.btn_plot_lines.setText(_translate("MainWindow", "Visualizar lineas"))
        self.btn_plot_areas.setText(_translate("MainWindow", "Visualizar planos"))
        self.classes_box.setTitle(_translate("MainWindow", "Clases"))

from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
from UI.resources import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

