# Algoritmo de Arbol Parcial Minimo de Prim

Descripción
Este proyecto implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST - Minimum Spanning Tree) en un grafo no dirigido y ponderado. El MST es un subconjunto de aristas que conecta todos los vértices del grafo sin ciclos y con el peso total mínimo posible.

Cómo funciona el algoritmo
El algoritmo de Prim sigue un enfoque voraz (greedy) para construir el MST:

Inicialización: Comienza seleccionando un nodo arbitrario como punto de partida.

Expansión: En cada iteración, añade la arista de menor peso que conecta un nodo ya incluido en el MST con uno que aún no está incluido.

Terminación: El proceso continúa hasta que todos los nodos del grafo estén incluidos en el MST.

El algoritmo utiliza una cola de prioridad (min-heap) para seleccionar eficientemente la siguiente arista con menor peso en cada paso.

Implementación
El código está estructurado en tres partes principales:

Definición del grafo: Representado como un diccionario donde cada clave es un nodo y su valor es una lista de tuplas (vecino, peso).

Función prim():

Mantiene un conjunto de nodos visitados

Usa una cola de prioridad para seleccionar aristas

Construye progresivamente el MST

Imprime el proceso paso a paso

Visualización:

Utiliza NetworkX para representar el grafo

Usa Matplotlib para mostrar gráficamente el MST resultante

Aplicación Real: Sistema de Transporte en una Fábrica
Contexto
Imaginemos una fábrica grande con múltiples estaciones de trabajo (nodos del grafo) que necesitan estar conectadas por un sistema de transporte (cintas transportadoras, tuberías o cables). Cada posible conexión entre estaciones tiene un costo asociado (peso de la arista) que puede representar:

Distancia física entre estaciones

Costo de instalación

Tiempo de transporte

Consumo energético

Nodos y sus significados
A: Estación de Recepción de Materias Primas

B: Área de Almacenamiento Primario

C: Estación de Ensamblaje Principal

D: Área de Control de Calidad

E: Estación de Empaquetado

F: Centro de Distribución

G: Almacén de Productos Terminados

H: Oficina de Supervisión

Conexiones y sus pesos
Las conexiones representan rutas posibles para instalar el sistema de transporte, con pesos que indican:

A-B (4): Conexión corta entre Recepción y Almacenamiento

A-H (8): Conexión directa entre Recepción y Supervisión

B-C (8): Conexión entre Almacenamiento y Ensamblaje

C-F (4): Ruta eficiente entre Ensamblaje y Distribución

F-G (2): Conexión crítica entre Distribución y Almacén Final

Beneficios del MST
Al aplicar el algoritmo de Prim:

Minimizamos costos totales: El MST garantiza la red de conexiones más económica

Eliminamos redundancias: No hay conexiones innecesarias

Mantenemos conectividad: Todas las estaciones quedan conectadas

Optimizamos recursos: Se priorizan las conexiones más eficientes

Resultado Esperado
Para esta fábrica, el MST óptimo podría ser:

A - B (4)

B - C (8)

C - F (4)

C - D (7)

D - E (9)

F - G (2)

A - H (8)

Este diseño conecta todas las estaciones con un costo total de 42 unidades, que es el mínimo posible.

Ejecución del Programa
El algoritmo comienza en la Estación de Recepción (A)

Selecciona progresivamente las conexiones más económicas

Muestra en consola cada paso del proceso

Finalmente, dibuja el MST resultante

 