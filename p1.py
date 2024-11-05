from arbol_avl import BinaryTree
from cola import Queue
from pila import Stack
from heap import HeapMin

pokemon_by_name = BinaryTree()
pokemon_by_number = BinaryTree()
pokemon_by_type = BinaryTree()

# LISTA 
pokemon_data = [
    {'name': 'Bulbasaur', 'number': 1, 'type': ['planta', 'veneno']},
    {'name': 'Charmander', 'number': 4, 'type': ['fuego']},
    {'name': 'Squirtle', 'number': 7, 'type': ['agua']},
    {'name': 'Jolteon', 'number': 135, 'type': ['eléctrico']},
    {'name': 'Lycanroc', 'number': 745, 'type': ['roca']},
    {'name': 'Tyrantrum', 'number': 697, 'type': ['roca', 'dragón']}
]

# Función para cargar datos en los tres árboles
def load_pokemon_data(pokemon_data):
    for pokemon in pokemon_data:
        pokemon_by_name.insert_node(pokemon['name'], pokemon)
        pokemon_by_number.insert_node(pokemon['number'], pokemon)
        for tipo in pokemon['type']:
            pokemon_by_type.insert_node(tipo, pokemon)

load_pokemon_data(pokemon_data)

def search_pokemon_by_approx_name_and_number(name_part, number=None):
    results = []

    def search_by_name(root, name_part):
        if root:
            if name_part.lower() in root.value.lower():
                if number is None or root.other_value['number'] == number:
                    results.append(root.other_value)
            search_by_name(root.left, name_part)
            search_by_name(root.right, name_part)

    search_by_name(pokemon_by_name.root, name_part)
    return results

print("Punto b) Búsqueda por nombre aproximado:")
print(search_pokemon_by_approx_name_and_number("bul"))

# Punto c
def show_pokemon_by_type(pokemon_type):
    def search_by_type(root, pokemon_type):
        if root:
            if root.value == pokemon_type:
                print(root.other_value['name'])
            search_by_type(root.left, pokemon_type)
            search_by_type(root.right, pokemon_type)
    search_by_type(pokemon_by_type.root, pokemon_type)

print("Punto c) Pokémon de tipo 'agua':")
show_pokemon_by_type("agua")

print("Punto d) Listado ascendente por número:")
pokemon_by_number.inorden()

print("Punto d) Listado por nivel por nombre:")
pokemon_by_name.by_level()

def show_specific_pokemon_data(names):
    for name in names:
        pokemon = pokemon_by_name.search(name)
        if pokemon:
            print(f"Datos de {name}: {pokemon.other_value}")
        else:
            print(f"{name} no encontrado.")

print("Punto e) Datos de Pokémon específicos:")
show_specific_pokemon_data(['Jolteon', 'Lycanroc', 'Tyrantrum'])

def count_pokemon_by_type(pokemon_type):
    def count_by_type(root, pokemon_type):
        count = 0
        if root:
            if root.value == pokemon_type:
                count += 1
            count += count_by_type(root.left, pokemon_type)
            count += count_by_type(root.right, pokemon_type)
        return count
    
    return count_by_type(pokemon_by_type.root, pokemon_type)

# Ejemplo de uso:
print("Punto f) Cantidad de Pokémon tipo 'eléctrico':", count_pokemon_by_type("eléctrico"))
print("Punto f) Cantidad de Pokémon tipo 'acero':", count_pokemon_by_type("acero"))

