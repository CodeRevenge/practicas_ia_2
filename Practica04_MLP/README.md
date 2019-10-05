# <center>Práctica 04: Multi Layer Adaline</center>
![PyPI - Python Version](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-blue)

## Uso
<p>Los siquientes elementos son necesarios para la ejecución del código</p>

+ Python 3.7.x
+ [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
+ PyQt 5
+ Qt Designer

### Instalar PyQt 5 y Qt Designer

```
conda update --all
conda install qt
conda install pyqt
```

### Iniciar el editor Qt

En el terminal ejecutar `designer` y abrir el archivo Interface_MLP.ui

### Convertir cambios a Python

Para que los cambios en el editor de interfaces surta efecto, es necesario ejecutar el siguiente comando que transformara el archivo `Interface_MLP.ui` en un archivo `Interface_MLP.py`

```
pyuic5 -x Interface_MLP.ui -o Interface_MLP.py
```

### Cambios de funcionalidades

Para agregar funcionalidades en el programa es necesario trabajar sobre el archivo `Interface_MLP.py` en la clase `MainWindow`

### Ejecutar programa

Para la ejecución del programa se debe hacer en la shell el siguiente comando

```
python "Main_MLP.py"
```



## Dependecias
+ [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
+ [Matplotlib](https://matplotlib.org/)
+ [Numpy](https://numpy.org/)

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)