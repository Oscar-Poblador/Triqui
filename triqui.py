tablero =[  "-", "-", "-",
             "-", "-", "-",
              "-", "-", "-"]
ganador = None
def jugar():
    global ganador
    print("Empieza a jugar")
    ver_tablero()
    for i in range(5):
        print("Turno del jugador 1 - Juega con X")
        valor="X"
        #empiezan a jugar - Jugador1
        jugada(valor)
        hayGanador()
        if (ganador != "X")&(i < 4) :
            for j in range(3):
                print("Turno del jugador 2 -Juega con O")
                valor="O"
                jugada(valor)
                hayGanador()
                if ganador == "O":
                    print("Felicadadesss!!! Jugador 2 GANADOR del TRIQUI :D ")
                break
        elif ganador=="X":
            print("Felicadadesss!!! Jugador 1 GANADOR del TRIQUI :D")
            break
        else:
            print("No hay ganador. El juego termina en EMPATE :/ ")
def hayGanador():
    global ganador
    controlLinea()
    controlVertical()
    controlDiagonal()
#Define si hay 3 en linea horizontal
def controlLinea():
    global ganador
    if tablero[0]== tablero[1]==tablero[2] !="-":
        ganador = tablero[0]
    elif tablero[3] ==  tablero[4] == tablero[5] != "-":
        ganador = tablero[3]
    elif tablero[6] ==  tablero[7] == tablero[8] != "-":
        ganador = tablero[6]
#Define si hay 3 en linea vertical
def controlVertical():
    global ganador
    if tablero[0] ==  tablero[3] == tablero[6] != "-":
        ganador = tablero[0]
    elif tablero[1] ==  tablero[4] == tablero[7] != "-":
        ganador = tablero[1]
    elif tablero[2] ==  tablero[5] == tablero[8] != "-":
        ganador = tablero[2]
#Define si hay 3 en linea diagonal
def controlDiagonal():
    global ganador
    if tablero[0] ==  tablero[4] == tablero[8] != "-":
        ganador = tablero[0]
    elif tablero[2] ==  tablero[4] == tablero[6] != "-":
        ganador = tablero[2]

def jugada(valor):
    anoto = False
    while anoto==False:
        posicion = int(input("Elegir una posicion del 1 al 9: "))
        posicion -= 1
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("\n////////////////////////////")
            print("Esa posicion ya esta ocupada")
            print("////////////////////////////\n")
    tablero[posicion] = valor
    ver_tablero()
def ver_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print("\n")
jugar()