from Backend import MainWindow, QtWidgets

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    if window.leerArchivo():
        window.normalizarDatos()
        window.show()
        app.exec_()


if __name__ == "__main__":
    main()