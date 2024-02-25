"""
=========================================================
Ejemplo de Regresión Lineal
=========================================================
El siguiente ejemplo utiliza solo la primera característica del conjunto de datos `diabetes`,
con el fin de ilustrar los puntos de datos dentro del gráfico bidimensional.
La línea recta se puede ver en el gráfico, mostrando cómo la regresión lineal
intenta trazar una línea recta que minimizará mejor la suma residual de los cuadrados
entre las respuestas observadas en el conjunto de datos,
y las respuestas predichas por la aproximación lineal.

También se calculan los coeficientes, la suma residual de los cuadrados y el coeficiente de
determinación.

"""

# Fuente del código: Jaques Grobler
# Licencia: BSD 3 cláusulas

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el conjunto de datos de diabetes
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Utilizar solo una característica
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Dividir los datos en conjuntos de entrenamiento/prueba
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Dividir los objetivos en conjuntos de entrenamiento/prueba
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Crear objeto de regresión lineal
regr = linear_model.LinearRegression()

# Entrenar el modelo usando los conjuntos de entrenamiento
regr.fit(diabetes_X_train, diabetes_y_train)

# Realizar predicciones usando el conjunto de prueba
diabetes_y_pred = regr.predict(diabetes_X_test)

# Los coeficientes
print("Coeficientes: \n", regr.coef_)
# El error cuadrático medio
print("Error cuadrático medio: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# El coeficiente de determinación: 1 es una predicción perfecta
print("Coeficiente de determinación: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Graficar resultados
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
