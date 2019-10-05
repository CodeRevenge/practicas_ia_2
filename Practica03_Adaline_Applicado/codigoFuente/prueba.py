import matplotlib.pylab as plt
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas
from PyQt5.QtWidgets import  QVBoxLayout, QWidget

layout = QVBoxLayout()
setLayout(layout)
x_data = np.array([1,2,3])
y_data = np.array([1,2,3])

fig, ax = plt.subplots()
linea, = ax.plot(x_data,y_data,'',alpha=0.8)
canvas = FigureCanvas(fig)    
layout.addWidget(canvas)
linea.set_ydata(y_data)
canvas.draw()