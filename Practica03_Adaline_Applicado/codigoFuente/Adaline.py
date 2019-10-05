import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Adaline:
    def __init__(self, entradas, clases, ratio_aprendizaje, epocas_maximas, pesos, theta, error_minimo):
        self.ERROR_MAX = 20

        self.entradas = np.array(entradas)
        self.salidas_deseadas = np.array(clases)
        self.ratio_aprendizaje = ratio_aprendizaje
        self.epocas_maximas = epocas_maximas
        self.pesos = np.array(pesos)
        self.theta = theta
        self.error_minimo = error_minimo
        self.errores = []
        

    def entrenamiento(self, ventana):
        progreso = ventana.progreso
        activacion = self.f_activacion()

        resultados = self.salidas_deseadas - activacion
        gradiente = activacion * (1-activacion)
        # error = (np.sum(np.array(resultados**2)))/len(self.pesos)
        error = (np.sum(np.array(resultados**2)))/len(self.pesos)
        self.epoca_actual = 0
        carga = 100 / self.epocas_maximas
        


        if error < self.error_minimo:
            self.errores.append(np.sum(resultados))
            self.cargarErrorGrafica(ventana)
            progreso.setValue(100)
            return True

        while self.epoca_actual < self.epocas_maximas and error > self.error_minimo:
            self.epoca_actual += 1
            i = 0
            progreso.setValue(self.epoca_actual * carga)

            self.theta = self.theta + (self.ratio_aprendizaje * resultados[i] * gradiente[i] * 1)
            for i,entrada in enumerate(self.entradas):
                self.pesos = self.pesos + (self.ratio_aprendizaje * resultados[i] * gradiente[i] * entrada)
                if error < self.error_minimo:
                    progreso.setValue(100)
                    return True
                
            activacion = self.f_activacion()
            resultados = self.salidas_deseadas - activacion
            gradiente = activacion * (1-activacion)
            error = (np.sum(np.array(resultados**2)))/len(self.pesos)
            self.errores.append(error)
            self.cargarErrorGrafica(ventana)

            # if len(self.errores) >= 100 and len(set(self.errores[-50:])):
            #     progreso.setValue(100)
            #     return False



        if error == 0 or error < self.error_minimo:
            progreso.setValue(100)
            return True

        return False

    def f_activacion(self):
        resultados = []
        net = np.dot(self.entradas, self.pesos) + self.theta
        # net = np.dot(self.entradas, self.pesos)
        for resultado in net:
            resultados.append(1 / (1 + math.exp(resultado*-1)))
        return np.array(resultados)

    def cargarErrorGrafica(self, ventana, error=[]):
        # self.linea_errores[1][-1] = error
        # self.linea_errores[1] = np.append(self.linea_errores[1][1:],0.0)
        # ventana.grafica_error.cargarGraficoDinamico(len(self.errores)-1,self.errores[-1] ,self.epocas_maximas, ventana.grafica_error.linea)
        pass