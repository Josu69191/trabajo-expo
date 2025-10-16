from collections import deque

def bfs(graph, start):
    """
    graph: dict donde clave = vértice, valor = lista de vecinos
    start: vértice inicial
    Retorna: diccionario dist que da la distancia (número de aristas) desde start a cada vértice alcanzable
    """
    dist = {v: None for v in graph}  # None para no visitado aún
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] is None:  # no ha sido visitado
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

# Ejemplo de uso:
if __name__ == "__main__":
    # Grafo de ejemplo (no dirigido)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    inicio = 'A'
    distancias = bfs(graph, inicio)
    print(f"Distancias desde {inicio}:")
    for v, d in distancias.items():
        print(f"  {v}: {d}")
