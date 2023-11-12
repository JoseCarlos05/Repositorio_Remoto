import math

def iswon():
    global ganador
    for i in range(0, 3):
        # Victoria en horizontal
        if (board[i][0] == board[i][1] == board[i][2]):
            ganador = board[i][0]
            return True
        # Victoria en vertical
        if (board[0][i] == board[1][i] == board[2][i]):
            ganador = board[0][i]
            return True
    # Victoria en diagonal de izquierda a derecha
    if (board[0][0] == board[1][1] == board[2][2]):
        ganador = board[0][0]
        return True
    # Victoria en diagonal de derecha a izquierda
    if (board[0][2] == board[1][1] == board[2][0]):
        ganador = board[0][2]
        return True
    return False

def printboard():
    for i in range(0, 3):
        print("+---------" * 3, "+", sep = '')
        print("|         " * 3, "|", sep = '')
        print("|    " + str(board[i][0]) + "    |    " +  str(board[i][1]) + "    |    " + str(board[i][2]) + "    |")
        print("|         " * 3, "|", sep = '')
    print("+---------" * 3, "+", sep = '')

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ganador = ""
turno = "X"

while iswon() == False:
    printboard()
    validselection = False
    while validselection == False:
        try:
            selection = int(input("Turno del jugador " + turno + ". HIJOS DE PUTA NO ME COPIEIS EL CODIGO:D "))
        # Si llegamos aquí es que el usuario no escribió un número entero
        except ValueError:
            continue
        # Sólo admitimos valores del 1 al 9
        if selection in range(1, 10):
            # Si dividimos el valor elegido, entre 3 y truncamos decimales obtenemos el índice de la línea donde está el usuario
            line = math.trunc((selection - 1) / 3)
            # Comprobamos si la selección todavía existe con ese valor en la línea indicada, pues esto significa que está libre
            if selection in board[line]:
                validselection = True
                # Actualizamos el valor nuevo
                board[line][board[line].index(selection)] = turno
                # Cambiamos el siguiente turno
                if turno == "X":
                    turno = "O"
                else:
                    turno = "X"

printboard()
print("Gana el jugador " + ganador)
