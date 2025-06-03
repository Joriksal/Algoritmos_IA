# 🧭 Simulador del Algoritmo de Dijkstra con Visualización

Este proyecto es un **simulador educativo** del algoritmo de **Dijkstra**, diseñado para mostrar paso a paso cómo se encuentra el camino más corto en un grafo. Incluye salidas en consola y una visualización gráfica para entender claramente cómo se seleccionan las rutas óptimas.

---

## 💡 ¿Qué resuelve este simulador?

Este simulador representa una situación común en la vida real: **encontrar la ruta más corta o eficiente** entre distintos puntos conectados.

🔌 Ejemplos de la vida real donde se aplica Dijkstra (simulados aquí):

- **Rutas de entrega**: Como una empresa de paquetería (tipo DHL o Amazon) que necesita entregar paquetes de forma eficiente. Cada nodo es una ciudad o punto de entrega, y las aristas (con peso) representan la distancia o el tiempo entre ubicaciones. El simulador encuentra el camino de entrega más rápido desde un centro de distribución.

- **Redes de telecomunicaciones**: Imagínate routers conectados entre sí. El algoritmo ayuda a encontrar el camino más rápido para que un paquete de datos llegue a su destino. Aquí, el peso puede representar la latencia o la carga de la red.

- **Videojuegos y GPS**: Dijkstra también se usa en videojuegos de estrategia o navegación GPS para calcular la mejor ruta evitando obstáculos o caminos largos.

---

## 🎯 ¿Qué hace este simulador?

- Calcula los **caminos más cortos** desde un nodo de origen a todos los demás.
- Imprime en consola **paso a paso** cómo se visitan los nodos y se actualizan las distancias.
- Muestra un **grafo visual**, donde los caminos más cortos se dibujan en **rojo**.
- Permite modificar fácilmente el grafo y el nodo de inicio.

---

## 🔍 Ejemplo aplicado del simulador

### 🗺️ Escenario simulado:

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

## 📦 Ejemplo aplicado de logística

Supón que cada nodo es una **sucursal** de una empresa de envíos, y los pesos representan los **costos de transporte** entre ellas.

Si el centro de distribución está en `'A'`, el objetivo es llegar al punto final `'G'` de la forma más económica posible.

✅ El simulador encuentra el camino más eficiente:

A → B → C → D → F → G (costo total: 8)


🔴 En cambio, otras rutas posibles como:

A → E → G (costo total: 15)

...resultan más caras, y por eso son descartadas.

Esta lógica es **idéntica** a cómo operaría un sistema de logística o una app de navegación en el mundo real.

---

### 🖥️ Salida real del simulador (resumen)

```bash
Visitando nodo: C con distancia actual: 3
 → Actualizando distancia de D de inf a 4
 → Actualizando distancia de E de inf a 6
...
Caminos más cortos:
 - A → G: A -> B -> C -> D -> F -> G


