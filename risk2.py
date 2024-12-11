from itertools import permutations, product

def generar_combinaciones(max_puntos, costos):
    """Genera todas las combinaciones posibles de tropas con restricciones."""
    combinaciones = []
    for infanteria, caballeria, artilleria in product(range(max_puntos + 1), repeat=3):
        costo_total = (infanteria * costos['infanteria'] + 
                       caballeria * costos['caballeria'] + 
                       artilleria * costos['artilleria'])
        if (costo_total <= max_puntos and 
            infanteria > 0 and caballeria > 0 and artilleria > 0):  # Debe haber al menos una de cada tipo
            combinaciones.append({'infanteria': infanteria, 'caballeria': caballeria, 'artilleria': artilleria})
    return combinaciones

def generar_permutaciones(territorios):
    """Genera todas las permutaciones posibles del orden de ataque."""
    return list(permutations(territorios))

def calcular_fuerza_total(tropas, fuerzas_tropas):
    """Calcula la fuerza total de un ejército."""
    return (tropas['infanteria'] * fuerzas_tropas['infanteria'] + 
            tropas['caballeria'] * fuerzas_tropas['caballeria'] + 
            tropas['artilleria'] * fuerzas_tropas['artilleria'])

def evaluar_estrategia(combinaciones, permutaciones, fuerzas_territorios, fuerzas_tropas):
    """Evalúa todas las estrategias posibles y selecciona las viables."""
    estrategias_viables = []
    for tropas in combinaciones:
        fuerza_inicial = calcular_fuerza_total(tropas, fuerzas_tropas)
        for orden in permutaciones:
            fuerza_total = fuerza_inicial
            es_viable = True
            for territorio in orden:
                if fuerza_total >= fuerzas_territorios[territorio]:
                    fuerza_total -= fuerzas_territorios[territorio]
                else:
                    es_viable = False
                    break
            if es_viable:
                estrategias_viables.append((tropas, orden))
    return estrategias_viables

def tablero_representado(fuerzas_territorios):
    """Representa el tablero de juego de manera visual."""
    print("\n=== Tablero ===")
    print("┌────────────┬────────────┬────────────┐")
    print("│ Territorio │ Fuerza     │            │")
    print("├────────────┼────────────┼────────────┤")
    for territorio, fuerza in fuerzas_territorios.items():
        print(f"│ {territorio:<10} │ {fuerza:<10} │ {'':<10} │")
    print("└────────────┴────────────┴────────────┘")

# Entrada de datos variable por parte del usuario
max_puntos = int(input("Introduce el máximo de puntos para el ejército: "))
costos = {
    'infanteria': int(input("Introduce el costo de la infantería: ")),
    'caballeria': int(input("Introduce el costo de la caballería: ")),
    'artilleria': int(input("Introduce el costo de la artillería: "))
}
fuerzas_tropas = {
    'infanteria': int(input("Introduce la fuerza de la infantería: ")),
    'caballeria': int(input("Introduce la fuerza de la caballería: ")),
    'artilleria': int(input("Introduce la fuerza de la artillería: "))
}
fuerzas_territorios = {}
num_territorios = int(input("Introduce el número de territorios enemigos: "))
for i in range(num_territorios):
    territorio = input(f"Introduce el nombre del territorio {i + 1}: ")
    fuerza = int(input(f"Introduce la fuerza de defensa del territorio {territorio}: "))
    fuerzas_territorios[territorio] = fuerza

# Generar combinaciones de tropas
combinaciones = generar_combinaciones(max_puntos, costos)

# Generar permutaciones de orden de ataque
permutaciones = generar_permutaciones(list(fuerzas_territorios.keys()))

# Evaluar estrategias
estrategias = evaluar_estrategia(combinaciones, permutaciones, fuerzas_territorios, fuerzas_tropas)

# Representar el tablero
tablero_representado(fuerzas_territorios)

# Mostrar solo estrategias viables
if estrategias:
    print("\n=== Estrategias Viables ===")
    for tropas, orden in estrategias:
        print(f"Tropas: {tropas} | Orden de ataque: {orden}")
else:
    print("\nNo se encontraron estrategias viables.")
