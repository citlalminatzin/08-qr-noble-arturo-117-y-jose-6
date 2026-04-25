[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23709736)
# Práctica 8

Este proyecto implementa herramientas para descomponer matrices y encontrar sus valores propios (eigenvalores) utilizando el algoritmo QR basado en la ortonormalización de Gram-Schmidt.

## Integrantes

- Góngora Ramírez Arturo
- Hernández Coutiño José de Jesús

## Uso

🚀 El proyecto está dividido en módulos jerárquicos para realizar las siguientes operaciones:
- gram_schmidt.py: Proceso de ortonormalización de vectores para generar bases ortogonales.
- qr.py: Descomposición de una matriz $A$ en el producto de una matriz ortogonal $Q$ y una triangular superior $R$.
- eigenvalues.py: Método iterativo para calcular los eigenvalores de una matriz mediante transformaciones de semejanza sucesivas.
- linearsolve.py: Este módulo permite resolver sistemas de ecuaciones lineales de la forma $Ax = b$. En lugar de utilizar la inversión de matrices (aprovechando propiedades de la Factorización QR)
- 
## Instalación

-  Python 3.10 o superior.

## Desarollo 
En este apartado se hace un pequeño resumen de las funciones involucradas en la resolución de los ejercicios y la matemática detrás de estas.
***

### Ejercicio 1

* Función principal:    ``resolver_polinomio_caracteristico_2x2(A)`` ubicada en ``main.py``.

* Cómo se resuelve: El problema requiere encontrar los eigenvalores de forma analítica para una matriz de $2\times 2$. En lugar de hacer llamadas numéricas, la función extrae la traza y el determinante de la matriz. Con estos dos valores, se construye el polinomio característico $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$. Posteriormente, se utiliza la fórmula general de las ecuaciones cuadráticas (considerando el discriminante) para encontrar las raíces exactas del polinomio, las cuales corresponden a los eigenvalores analíticos.

### Ejercicio 2

* Función principal: ``eigenvals(A, n)`` ubicada en ``eigenvalues.py``.

* Funciones de apoyo: ``qr(A_k)`` (para la factorización) y ``matmul(R, Q)`` (para la multiplicación), ambas alimentadas por el proceso de Gram-Schmidt.

* Cómo se resuelve: Este ejercicio implementa el algoritmo iterativo de forma estricta por un número definido de pasos. En cada iteración, la matriz actual $A_{k}$ se descompone en una matriz ortogonal $Q$ y una triangular superior $R$. Inmediatamente después, se calcula la siguiente matriz iterada invirtiendo el orden de la multiplicación: $A_{k+1} = R_{k}Q_{k}$. Tras ejecutar el ciclo exactamente 10 veces, el algoritmo asume que los valores en la diagonal principal de la matriz resultante son aproximaciones razonables de los eigenvalores reales y los extrae.

### Ejercicio 3

* Función principal: ``eigenvals_tol(A, max_iter, tol)`` ubicada en ``eigenvalues.py``.

* Funciones de apoyo: Igualmente depende de ``qr(A_k)`` y ``matmul(R, Q)``.

* Cómo se resuelve: Este problema busca controlar la precisión del algoritmo iterativo. La lógica base de factorización y multiplicación es la misma que en el Ejercicio 2, pero se introduce una validación en cada iteración. El programa recorre todas las entradas que están fuera de la diagonal principal y encuentra el valor absoluto máximo. Si este valor máximo es estrictamente menor a la tolerancia definida ($\epsilon = 1\times 10^{-10}$), el ciclo se rompe prematuramente, garantizando que la matriz es prácticamente diagonal. Si no se alcanza esta convergencia, el algoritmo tiene una red de seguridad y se detiene al llegar a las 1000 iteraciones para evitar ciclos infinitos.

## Conclusiones

Al contrastar los tres métodos empleados para el cálculo de los eigenvalores de la matriz $A$, se aprecia claramente la transición teórica y la utilidad de las aproximaciones numéricas frente a las soluciones analíticas.

En el Ejercicio 1 el método algebraico del polinomio característico arrojó los valores exactos de $\lambda_1 = 9$ y $\lambda_2 = 4$. Al ser un sistema cerrado, este cálculo nos proporciona la "verdad" contra la cual podemos evaluar rigurosamente el margen de error de nuestros algoritmos iterativos. En el Ejercicio 2, al ejecutar el algoritmo QR simple con un límite arbitrario de 10 iteraciones, obtuvimos $\lambda_1 \approx 8.999998$ y $\lambda_2 \approx 4.000002$. Esto demuestra empíricamente el comportamiento asintótico del algoritmo; es decir, conforme el número de iteraciones crece, los valores propios de la matriz iterada se aproximan a los valores propios exactos de la matriz original $A$. Por último, en el Ejercicio 3 la introducción de una restricción por tolerancia ($\epsilon = 1\times 10^{-10}$) revela la potencia de este método en el análisis numérico. El algoritmo requirió 32 iteraciones para estabilizarse, logrando empatar la exactitud del cálculo analítico hasta el décimo decimal ($\lambda_1 = 9.0000000000$ y $\lambda_2 = 4.0000000000$). Esto valida directamente el teorema central de la práctica, el cual establece que, al ser $A$ una matriz simétrica, la sucesión de matrices iteradas $A_k$ converge exitosamente a una matriz diagonal con los eigenvalores en la diagonal principal.