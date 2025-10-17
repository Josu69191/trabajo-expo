# Representamos un grafo como un diccionario.
# Cada clave es un nodo y su valor es una lista de los nodos conectados a él.
grafo = {
    'A': ['B', 'C'],   # El nodo A está conectado con B y C
    'B': ['D', 'E'],   # El nodo B está conectado con D y E
    'C': ['F'],        # El nodo C está conectado con F
    'D': [],           # El nodo D no tiene conexiones
    'E': ['F'],        # El nodo E se conecta con F
    'F': []            # El nodo F no tiene conexiones
}

# Función para realizar un recorrido en anchura (BFS - Breadth-First Search)
def bfs(grafo, inicio):
    visitados = []       # Lista donde guardaremos los nodos visitados
    cola = [inicio]      # Cola (lista) donde se agregan los nodos por visitar

    while cola:  # Mientras haya elementos en la cola
        nodo = cola.pop(0)  # Sacamos el primer nodo (FIFO: primero en entrar, primero en salir)

        if nodo not in visitados:  # Si aún no lo hemos visitado
            visitados.append(nodo)  # Lo agregamos a la lista de visitados
            vecinos = grafo[nodo]   # Obtenemos los vecinos (nodos conectados)
            cola.extend(vecinos)    # Los agregamos a la cola para visitarlos después

    return visitados  # Retornamos el orden en que visitamos los nodos

# Probamos la función BFS empezando desde el nodo 'A'
resultado = bfs(grafo, 'A')
print("Recorrido BFS desde A:", resultado)

