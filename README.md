# fantastic-guacamole

## Documentación: Error Cuadrático Medio y Coeficiente de Determinación

Este README es una traducción al lenguaje español creada por ChatGPT de la documentación oficial para entender el Error Cuadrático Medio (ECM) y el Coeficiente de Determinación en el contexto de la regresión lineal.

### Error Cuadrático Medio (ECM)

El Error Cuadrático Medio (ECM) es una medida de la calidad de la predicción de un modelo de regresión. Se calcula como la media de los cuadrados de las diferencias entre los valores reales y los valores predichos por el modelo.

La fórmula matemática del ECM es:

$$ECM = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y_i})^2$$
donde:
- $( n )$ es el número de observaciones.
- $( y_i )$ es el valor real del objetivo para la i-ésima observación.
- $( \hat{y_i} )$ es el valor predicho por el modelo para la i-ésima observación.

Un ECM más bajo indica un mejor ajuste del modelo a los datos.

### Coeficiente de Determinación (R cuadrado)

El coeficiente de determinación, comúnmente denotado como $( R^2 )$, es una medida que indica la proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes en el modelo de regresión.

La fórmula matemática del coeficiente de determinación es:


$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y_i})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

donde:
- $( n )$ es el número de observaciones.
- $( y_i )$ es el valor real del objetivo para la i-ésima observación.
- $( \hat{y_i} )$ es el valor predicho por el modelo para la i-ésima observación.
- $( \bar{y} )$ es la media de los valores reales del objetivo.

El coeficiente de determinación varía entre 0 y 1. Un $( R^2 )$ más cercano a 1 indica un mejor ajuste del modelo a los datos.

---

Esta traducción fue realizada por ChatGPT con fines educativos y de divulgación.
