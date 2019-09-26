from Adaline_Aplicado_UI import QtWidgets, Ui_MainWindow
from Adaline import Adaline
from mplwidget import MplWidget
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, MplWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.ARCHIVO_BASE = 'divorce_reduced.csv'

        self.btn_Entrenar.clicked.connect(self.entrenar_adaline)
        self.btn_Predecir.clicked.connect(self.realizar_prediccion)

        items = ['0','1','2','3','4']
        self.cb_1.addItems(items)
        self.cb_2.addItems(items)
        self.cb_3.addItems(items)
        self.cb_4.addItems(items)
        self.cb_5.addItems(items)
        self.cb_6.addItems(items)
        self.cb_1.setCurrentIndex(0)
        self.cb_2.setCurrentIndex(0)
        self.cb_3.setCurrentIndex(0)
        self.cb_4.setCurrentIndex(0)
        self.cb_5.setCurrentIndex(0)
        self.cb_6.setCurrentIndex(0)
        

        # self.lineaErrores[1][-1] = 0
        # self.lineaErrores[1] = np.append(self.lineaErrores[1][1:],0.0)
        # grafica.cargarGrafica(self.ERROR_MAX, self.lineaErrores[0], self.lineaErrores[1], grafica.linea, False)



    def leerArchivo(self):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setIcon(QtWidgets.QMessageBox.Warning)
        mensaje.setText("Falta el archivo " + self.ARCHIVO_BASE)
        mensaje.setInformativeText("Es necesario que selecciones un archivo *.csv para continuar con la ejecución")
        mensaje.setWindowTitle("Fallo la selección de archivo")
        mensaje.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Cancel)
        mensaje.setDefaultButton(QtWidgets.QMessageBox.Retry)

        orden = True

        while orden:
            try:
                self.datos = pandas.read_csv(self.ARCHIVO_BASE)
                return True
            except FileNotFoundError:
                orden = mensaje.exec_()
                    # 4194304 código de retorno para boton cancelar
                if orden == 4194304:
                    orden = False
                else:
                    nombre_archivo = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", ".", "Procesos (*.csv)")
                    self.direccionArchivo = nombre_archivo
                    if nombre_archivo != "":
                        orden = False
                        self.datos = pandas.read_csv(nombre_archivo[0])
                        return True
                    else:
                        orden = mensaje.exec_()
                        # 4194304 código de retorno para boton cancelar
                        if orden == 4194304:
                            orden = False
        return False

    def entrenar_adaline(self):
        ratio_aprendizaje = self.sb_ratio.value()
        epocas_maximas = self.sb_epocas.value()
        error_minimo = self.sb_error.value()
        entradas = np.array(self.datos.iloc[:,:-1].values.tolist())
        clases = np.array(sum(self.datos.iloc[:,-1:].values.tolist(),[]))
        pesos = np.random.rand(len(self.datos.columns)-1)
        theta = np.random.rand()

        self.btn_Entrenar.setEnabled(False)
        self.adaline = Adaline(entradas, clases, ratio_aprendizaje, epocas_maximas, pesos, theta, error_minimo)
        convergencia = self.adaline.entrenamiento(self)

        if convergencia:
            self.lbl_convergencia.setText("Sí convergió en " + str(self.adaline.epoca_actual) + " épocas")
            self.pruebas.setEnabled(True)
            self.btn_Predecir.setEnabled(True)
            self.resultados.setEnabled(True)
        else:
            self.lbl_convergencia.setText("No convergió")

        self.lbl_error_minimo.setText("El error mínimo alcanzado es: " + "{:10.4f}".format(self.adaline.errores[-1]))

        self.graficar()

        self.btn_Entrenar.setEnabled(True)


    def realizar_prediccion(self):
        atr1 = int(self.cb_1.currentText())
        atr2 = int(self.cb_2.currentText())
        atr3 = int(self.cb_3.currentText())
        atr4 = int(self.cb_4.currentText())
        atr5 = int(self.cb_5.currentText())
        atr6 = int(self.cb_6.currentText())

        entradas = np.array([atr1, atr2, atr3, atr4, atr5, atr6])

        dot = np.dot(entradas, self.adaline.pesos) + self.adaline.theta
        
        if dot > 0:
            self.resultado.setText("Resultado:\nSe van a divorciar")
        else:
            self.resultado.setText("Resultado:\nNo se van a divorciar")

    def graficar(self):
        # fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

        # ax.plot(range(1, len(self.adaline.errores) + 1), self.adaline.errores)
        # ax.set_xlabel('Épocas')
        # ax.set_ylabel('Errores')
        # ax.set_title('Adaline aplicado')

        # plt.tight_layout()
        # plt.show()

        self.grafica_error.cargarGrafico(range(1, len(self.adaline.errores) + 1), self.adaline.errores)