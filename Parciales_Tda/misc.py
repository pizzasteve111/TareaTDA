def min_vertex_cover_greedy(grafo):
    cover=[]
    visitados=set()
    vertices=grafo.obtener_vertices()
    actual=vertices[0]
    while len(visitados)!=len(vertices):
        
