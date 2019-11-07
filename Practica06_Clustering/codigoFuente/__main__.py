import sys
from UI.ui_backend import UI_Backend, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Backend()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass