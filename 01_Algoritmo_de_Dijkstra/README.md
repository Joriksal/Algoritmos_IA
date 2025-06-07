# Simulador del Algoritmo de Dijkstra con Visualización

Este proyecto es un simulador del algoritmo de Dijkstra, diseñado para mostrar paso a paso cómo se encuentra el camino más corto en un grafo. Incluye salidas en consola y una visualización gráfica para entender claramente cómo se seleccionan las rutas óptimas.

## ¿Qué problema resuelve este simulador?

Este simulador representa una situación común en la vida real: **encontrar la ruta más corta o eficiente** entre distintos puntos conectados, para ser mas concretos se determina un nodo de origen y a partir de ese busca el camino mas corto a todos los demas nodos que quedan.

# Aplicaciones reales simuladas en este proyecto:

- **Logisitica y rutas de entregas**: Modela un sistema de distribucion de paquetes, donde cada nodo representa una sucursal o punto de entrega, y las conexiones entre ellos tienen costo asociado (distancia, tiempo o dinero). El algoritmo permite encontrar la ruta mas barata desde un centro de distribucion hacia los destinos.

- **Redes de telecomunicaciones**: Los nodos representan dispositivos como routers, y las conexiones ponderadas simulan el retrdo o el costo de transmision. El algortimo permite hallar el camino mas rpaido o confiable para enviar datos.

- **Sistemas de navegacion y videojuego**: En aplicaciones GPS o videojuegos de estrategia. Dijkstra se emplea para calcular rutas optimas evitando caminos largos o bloqueados.

---

## ¿Qué hace este simulador?

- Calcula los **caminos más cortos** desde un nodo de origen a todos los demás.
- Imprime en consola **paso a paso** cómo se visitan los nodos y se actualizan las distancias.
- Muestra un **grafo visual**, donde los caminos más cortos se dibujan en **rojo**.
- Permite modificar fácilmente el grafo y el nodo de inicio.

### Escenario simulado en el codigo:
El grafo representado en el cosigo contiene los siguientes nodos y conexiones:

    ```python
    [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('C', 'E', 3),
        ('D', 'F', 2),
        ('E', 'F', 1),
        ('E', 'G', 5),
        ('F', 'G', 2),
        ('B', 'E', 7),
        ('A', 'E', 10)
    ]
    ```

## Ejemplo aplicado: logistica de distribucion

Supongamos que la empresa desea enviar un paquete desde la sucursal A (Centro de distribucion) hasta la sucursal G (destino final). El objetivo es minimizar el costo total del trayecto.
El simulador aplcia el algoritmo de Dikstra para encontrar la ruta de menor costo. En este caso, el resultado es:

## Ruta optima:

A → B → C → D → F → G (costo total: 8)

En cambio, otras rutas posibles como:

A → E → G (costo total: 15)

...resultan más caras, y por eso son descartadas.

Esta lógica es **idéntica** a cómo operaría un sistema de logística o una app de navegación en el mundo real.

---

### Salida real del simulador (resumen)

```bash
Visitando nodo: C con distancia actual: 3
 → Actualizando distancia de D de inf a 4
 → Actualizando distancia de E de inf a 6
...
Caminos más cortos:
 - A → G: A -> B -> C -> D -> F -> G


