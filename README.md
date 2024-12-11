# Juego de Estrategia RISK

LINK REPOSITORIO: https://github.com/mariamunoznadales/risk1.git

Este programa simula un juego de estrategia en el que puedes crear combinaciones de tropas y planificar un ataque a territorios enemigos. Genera todas las combinaciones posibles de tropas respetando los recursos disponibles y evalúa las estrategias viables de ataque, considerando el orden de los territorios y las restricciones de recursos.

## Características

1. **Generación de combinaciones de tropas**: 
   - Las combinaciones se generan respetando un límite de puntos disponibles (por defecto 20 puntos).
   - El ejército debe tener al menos una unidad de infantería, caballería y artillería.
   
2. **Generación de permutaciones de ataque**:
   - El orden de ataque a los territorios enemigos se genera como todas las permutaciones posibles de los territorios.
   
3. **Evaluación de estrategias**:
   - El programa calcula la fuerza total del ejército y evalúa si puede derrotar a todos los territorios enemigos en el orden dado.
   
4. **Entrada de datos variable**:
   - Los valores del juego (máximo de puntos, costos de tropas, fuerzas de tropas, territorios enemigos) son ingresados por el usuario a través de la consola.

5. **Representación visual del tablero**:
   - El tablero de juego se presenta como una tabla con los territorios enemigos y sus respectivas fuerzas de defensa.
  
## Instrucciones

Ingresa los datos cuando se te soliciten:

- El máximo de puntos disponibles para crear las tropas.
- El costo de cada tipo de tropa (infantería, caballería y artillería).
- La fuerza de cada tipo de tropa.
- El número de territorios enemigos y la fuerza de cada uno.

Visualiza el tablero de los territorios enemigos con sus fuerzas de defensa.

Revisa las estrategias viables que el programa ha encontrado, junto con las combinaciones de tropas y los órdenes de ataque correspondientes.

