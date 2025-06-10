# Algoritmo de Árbol de Expansión Mínima de Kruskal

## Descripción  
Este proyecto implementa el **algoritmo de Kruskal** para encontrar el **Árbol de Expansión Mínima** (MST - *Minimum Spanning Tree*) en un grafo no dirigido y ponderado. El MST conecta todos los vértices del grafo con el menor costo total posible y sin formar ciclos.

## Cómo funciona el algoritmo de Kruskal  
El algoritmo de Kruskal sigue un enfoque **voraz (greedy)** para construir el MST:

1. **Ordenar las aristas:** Se listan todas las aristas del grafo y se ordenan por peso (de menor a mayor).  
2. **Agregar aristas válidas:** Se recorren las aristas ordenadas, y se agrega una al MST **solo si no forma un ciclo**.  
3. **Unión de conjuntos:** Se usa una estructura llamada **Unión-Find (Union-Find o Disjoint Set)** para detectar si al agregar una arista se forma un ciclo.  
4. **Finalización:** El proceso continúa hasta que el MST tenga exactamente **(n - 1)** aristas, donde **n** es el número de nodos.

## Implementación  
El código tiene las siguientes partes clave:

- **Representación del grafo:**  
  Una lista de tuplas que contiene las aristas con el formato `(peso, nodo1, nodo2)`.

- **Función `kruskal()`:**  
  - Ordena todas las aristas por peso.  
  - Usa el algoritmo Union-Find para evitar ciclos.  
  - Agrega las aristas válidas al MST y muestra cada paso.  
  - Devuelve el MST final.

- **Visualización:**  
  - Usa la librería **NetworkX** para construir y dibujar el grafo.  
  - Utiliza **Matplotlib** para mostrar gráficamente el MST resultante, resaltando las aristas seleccionadas.

## Aplicación Real: Red de Comunicaciones en una Planta Industrial

### Contexto  
Imaginemos una planta industrial con distintos módulos que necesitan estar interconectados por una red de comunicaciones (cableado de red, fibra óptica, etc.). Las conexiones entre módulos tienen costos asociados (longitud, dificultad de instalación, etc.).

### Nodos y su significado

| Nodo | Módulo                                |
|------|----------------------------------------|
| A    | Oficina Principal                      |
| B    | Centro de Control                      |
| C    | Planta de Producción                   |
| D    | Laboratorio de Pruebas                 |
| E    | Sala de Servidores                     |
| F    | Estación de Monitoreo                  |
| G    | Taller de Mantenimiento                |
| H    | Área de Logística                      |

### Conexiones y pesos

| Conexión | Peso | Descripción                                  |
|----------|------|----------------------------------------------|
| A - B    | 4    | Cableado principal entre Oficina y Control   |
| A - H    | 8    | Enlace largo hacia Logística                 |
| B - C    | 8    | Conexión entre Control y Producción          |
| C - F    | 4    | Enlace de producción a Monitoreo             |
| F - G    | 2    | Ruta entre Monitoreo y Mantenimiento         |
| C - D    | 7    | Conexión a Laboratorio                       |
| D - E    | 9    | Enlace del Laboratorio a Sala de Servidores |

## Beneficios del MST con Kruskal

- **Costos mínimos:** Solo se agregan las conexiones más baratas posibles sin crear ciclos.  
- **Alta eficiencia:** Garantiza conectividad completa entre módulos con el menor cableado necesario.  
- **Evita redundancias:** No se agregan enlaces que no aporten a la conectividad.  
- **Adaptabilidad:** Fácil de aplicar en redes grandes gracias a su enfoque por aristas.

## Resultado Esperado

Para esta red de planta, el MST óptimo podría ser:

- A - B (4)  
- B - C (8)  
- C - D (7)  
- C - F (4)  
- F - G (2)  
- D - E (9)  
- A - H (8)

Esto da un costo total mínimo de **42 unidades**, conectando todos los módulos sin ciclos.

## Ejecución del Programa

- El algoritmo toma todas las conexiones posibles, las ordena y selecciona las mejores.  
- Muestra por consola el proceso de selección de aristas paso a paso.  
- Al final, se dibuja el grafo con el MST resaltado para visualizar la solución.
