[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23709736)
# Práctica 8

¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO
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
### Instalación

-  Python 3.10 o superior.
