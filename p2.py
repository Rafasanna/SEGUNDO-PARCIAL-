from grafo import Graph 

print("PUNTO A")
# Punto a: Crear el grafo y cargar los personajes
star_wars_graph = Graph(dirigido=False)

characters = [
    ('Luke Skywalker', 'Darth Vader', 4),
    ('Luke Skywalker', 'Leia', 5),
    ('Darth Vader', 'Yoda', 3),
    ('Leia', 'Han Solo', 5),
    ('Leia', 'C-3PO', 6),
    ('Han Solo', 'Chewbacca', 7),
    ('Yoda', 'Chewbacca', 3),
    ('Leia', 'Rey', 2),
    ('Kylo Ren', 'Rey', 4),
    ('Luke Skywalker', 'R2-D2', 6),
    ('Luke Skywalker', 'BB-8', 1),
    ('R2-D2', 'C-3PO', 8),
    ('Han Solo', 'Boba Fett', 3)
]

for char1, char2, episodes in characters:
    star_wars_graph.insert_vertice(char1)
    star_wars_graph.insert_vertice(char2)
    star_wars_graph.insert_arista(char1, char2, episodes)

print("PUNTO B")
# Punto b
def contains_yoda(tree):
    for arbol in tree:
        if 'Yoda' in arbol:
            return True
    return False

min_spanning_tree = star_wars_graph.kruskal('Luke Skywalker')
print("Árbol de expansión mínimo contiene a Yoda:", contains_yoda(min_spanning_tree))
print("Árbol de expansión mínimo:", min_spanning_tree)

print("PUNTO C")
# Punto c
def max_shared_episodes(graph):
    max_episodes = 0
    max_pair = None

    for nodo in graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_episodes:
                max_episodes = arista['peso']
                max_pair = (nodo['value'], arista['value'])

    return max_pair, max_episodes

max_pair, max_episodes = max_shared_episodes(star_wars_graph)
print(f"Máximo de episodios compartidos: {max_episodes}, entre {max_pair[0]} y {max_pair[1]}")

print("PUNTO D")
# Punto D
def cargar_personajes(graph, personajes):
    for personaje in personajes:
        graph.insert_vertice(personaje)

personajes_necesarios = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 'Leia', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8']
cargar_personajes(star_wars_graph, personajes_necesarios)

print("\nPersonajes cargados en el grafo:")
star_wars_graph.show_graph()
