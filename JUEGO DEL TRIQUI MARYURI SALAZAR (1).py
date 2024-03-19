# Hacer un triki 
# Maryuri Salazar 

def tablerodejuego(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def ganador(tablero, simbolo):
    for fila in tablero:
        if all(cell == simbolo for cell in fila):
            return True

    for col in range(3):
        if all(tablero[row][col] == simbolo for row in range(3)):
            return True

    if all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True

    return False

def triqui():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    while True:
        tablerodejuego(tablero)
        turnoactual = jugadores[turno % 2]
        print(f"Turno del jugador {turnoactual}")

        fila = int(input("Ingrese la fila (0, 1, 2): "))
        col = int(input("Ingrese la columna (0, 1, 2): "))

        if tablero[fila][col] != " ":
            print("La casilla ya está ocupada. Intente de nuevo.")
            continue

        tablero[fila][col] = turnoactual

        if ganador(tablero, turnoactual):
            tablerodejuego(tablero)
            print(f"¡El jugador {turnoactual} ha ganado!")
            break

        if all(all(cell != " " for cell in fila) for fila in tablero):
            tablerodejuego(tablero)
            print("¡Empate!")
            break

        turno += 1

if __name__ == "__main__":
    triqui()
 