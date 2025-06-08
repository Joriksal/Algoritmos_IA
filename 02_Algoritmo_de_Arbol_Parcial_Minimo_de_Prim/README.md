# Algoritmo de Arbol Parcial Minimo de Prim

## Descripción
Este proyecto implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST - Minimum Spanning Tree) en un grafo no dirigido y ponderado. El MST es un subconjunto de aristas que conecta todos los vértices del grafo sin ciclos y con el peso total mínimo posible.

## Cómo funciona el algoritmo de Prim
El algoritmo de Prim sigue un enfoque voraz (greedy) para construir el MST:

1. **Inicialización:** Comienza seleccionando un nodo arbitrario como punto de partida.

2. **Expansión:** En cada iteración, añade la arista de menor peso que conecta un nodo ya incluido en el MST con uno que aún no está incluido.

3. **Terminación:** El proceso continúa hasta que todos los nodos del grafo estén incluidos en el MST.

El algoritmo utiliza una cola de prioridad (min-heap) para seleccionar eficientemente la siguiente arista con menor peso en cada paso.

## Implementación
El código está estructurado en tres partes principales:

- **Definición del grafo:**
Representado como un diccionario donde cada clave es un nodo y su valor es una lista de tuplas (vecino, peso).

- **Función `prim()`:**

    - Mantiene un conjunto de nodos visitados.  
    - Usa una cola de prioridad para seleccionar las aristas más económicas.  
    - Construye progresivamente el MST, agregando aristas y visitando nodos nuevos.  
    - Imprime en consola cada paso de la construcción para facilitar la comprensión.

- **Visualización:**  

    - Utiliza la librería **NetworkX** para crear la estructura del grafo.  
    - Usa **Matplotlib** para mostrar gráficamente el MST resultante con etiquetas de pesos.

## Aplicación Real: Sistema de Transporte en una Fábrica

### Contexto

Imaginemos una fábrica grande con múltiples estaciones de trabajo (nodos del grafo) que necesitan estar conectadas por un sistema de transporte (cintas transportadoras, tuberías o cables). Cada posible conexión entre estaciones tiene un costo asociado (peso de la arista) que puede representar:

- Distancia física entre estaciones  
- Costo de instalación  
- Tiempo de transporte  
- Consumo energético  

### Nodos y su significado

| Nodo | Estación                              |
|-------|-------------------------------------|
| A     | Estación de Recepción de Materias Primas |
| B     | Área de Almacenamiento Primario     |
| C     | Estación de Ensamblaje Principal    |
| D     | Área de Control de Calidad           |
| E     | Estación de Empaquetado              |
| F     | Centro de Distribución               |
| G     | Almacén de Productos Terminados     |
| H     | Oficina de Supervisión               |

### Conexiones y pesos

Las conexiones representan rutas posibles para instalar el sistema de transporte, con pesos que indican:

| Conexión | Peso | Descripción                        |
|----------|------|----------------------------------|
| A - B    | 4    | Conexión corta entre Recepción y Almacenamiento |
| A - H    | 8    | Conexión directa entre Recepción y Supervisión   |
| B - C    | 8    | Conexión entre Almacenamiento y Ensamblaje       |
| C - F    | 4    | Ruta eficiente entre Ensamblaje y Distribución   |
| F - G    | 2    | Conexión crítica entre Distribución y Almacén Final |

## Beneficios del MST en esta aplicación
Al aplicar el algoritmo de Prim:

- **Minimización de costos totales:** El MST garantiza la red de conexiones más económica posible.  
- **Eliminación de redundancias:** No se incluyen conexiones innecesarias, evitando costos adicionales.  
- **Conectividad garantizada:** Todas las estaciones quedan conectadas mediante rutas optimizadas.  
- **Optimización de recursos:** Se priorizan las conexiones más eficientes para maximizar el rendimiento.


## Resultado Esperado
Para esta fábrica, el MST óptimo podría ser:

- A - B (4)
- B - C (8)
- C - F (4)
- C - D (7)
- D - E (9)
- F - G (2)
- A - H (8)

Este diseño conecta todas las estaciones con un costo total de 42 unidades, que es el mínimo posible.

## Ejecución del Programa

- El algoritmo comienza en la **Estación de Recepción (A)**.  
- Selecciona progresivamente las conexiones más económicas.  
- Muestra en consola cada paso del proceso para facilitar el seguimiento.  
- Finalmente, dibuja el MST resultante con todas las conexiones y sus pesos para visualización.

 