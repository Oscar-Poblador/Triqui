from re import A
import random

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
        jugada(valor,48)
        hayGanador()
        if (ganador != "X")&(i < 4) :
            for j in range(3):
                
                valor="O"
                jugada(valor,juega_maquina())
                hayGanador()
                if ganador == "O":
                    print("La MAQUINA ha ganado el triqui :u")
                    menu()
                break
        elif ganador=="X":
            print("Felicadadesss!!! Jugador 1 GANADOR del TRIQUI :D")
            menu()
            break
        else:
            print("No hay ganador. El juego termina en EMPATE :/ ")
            menu()
def menu():
    aux=int(input('\nSi desea seguir jugando ingrese el 0 sino el 1: '))
    if (aux==0):
        vaciar()
        jugar()
    else:
        print('Gracias por jugar')
        exit(0)
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

def jugada(valor,i):
    anoto = False
    while anoto==False:
        if(i==48):
            posicion = int(input("Elegir una posicion del 1 al 9: "))
            posicion -= 1
        else:
            posicion=i
            
            
        if tablero[posicion] == "-":
            print('si')
            anoto = True
        else:
            print("\n////////////////////////////")
            print("Esa posicion ya esta ocupada")
            print("////////////////////////////\n")
            i=48
            ver_tablero()
    tablero[posicion] = valor
    ver_tablero()
def juega_maquina():
    anoto = False
    while anoto==False:
        
        
        if(tablero[0]!='-')|(tablero[2]!='-')|(tablero[6]!='-')|(tablero[8]!='-')|(tablero[5]!='-')&(tablero[4]=='-'):
            posicion=5
            empatar=1
            
        if(empatar==1)&(tablero[4]!='-'):
            opc=0
            if(tablero[6]=='X'):
                if(tablero[3]=='X'):
                    posicion=1
                    opc=1
                if(tablero[0]=='X'):
                    posicion=4
                    opc=1
                if(tablero[7]=='X'):
                    posicion=9
                    opc=1
                if(tablero[8]=='X'):
                    posicion=8
                    opc=1
                if(tablero[1]=='X'):
                    posicion=4
                    opc=1
                if(tablero[5]=='X'):
                    posicion=8
                    opc=1
            if(tablero[0]=='X'):
                if(tablero[3]=='X'):
                    posicion=7
                    opc=1
                if(tablero[6]=='X'):
                    posicion=4
                    opc=1
                if(tablero[1]=='X'):
                    posicion=3
                    opc=1
                if(tablero[2]=='X'):
                    posicion=2
                    opc=1
                if(tablero[5]=='X'):
                    posicion=2
                    opc=1
                if(tablero[7]=='X'):
                    posicion=4
                    opc=1
            
            if(tablero[2]=='X'):
                if(tablero[1]=='X'):
                    posicion=1
                    opc=1
                if(tablero[0]=='X'):
                    posicion=2
                    opc=1
                if(tablero[5]=='X'):
                    posicion=9
                    opc=1
                if(tablero[8]=='X'):
                    posicion=6
                    opc=1
                if(tablero[3]=='X'):
                    posicion=2
                    opc=1
                if(tablero[7]=='X'):
                    posicion=6
                    opc=1
            if(tablero[8]=='X'):
                if(tablero[5]=='X'):
                    posicion=3
                    opc=1
                if(tablero[2]=='X'):
                    posicion=6
                    opc=1
                if(tablero[7]=='X'):
                    posicion=7
                    opc=1
                if(tablero[6]=='X'):
                    posicion=8
                    opc=1
                if(tablero[3]=='X'):
                    posicion=8
                    opc=1
                if(tablero[1]=='X'):
                    posicion=6
                    opc=1
            if(tablero[1]=='X')&(tablero[5]=='X'):
                posicion=1
            if(tablero[0]=='X')&(tablero[1]=='X'):
                posicion=3
            if(tablero[1]=='X')&(tablero[8]=='X'):
                posicion=3
            if(tablero[1]=='X')&(tablero[5]=='X')&(tablero[6]):
                posicion=3
            
            
            
            #if(tablero[3]=='O'):
              #  posicion=6
             #   opc=2
            #if(tablero[5]=='O'):
              #  posicion=4
             #   opc=2

            #if(tablero[1]=='O'):
                #posicion=8
               # opc=2
            #if(tablero[7]=='O'):
                #posicion=2
                #opc=2
            
                

            

                
                
        posicion-=1   
       
        if tablero[posicion] == "-":
            print('a')
            anoto = True
        
        else:
            anoto= False
    return posicion



def ver_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print("\n")
def vaciar():
    global ganador
    ganador=None
    for i in range(9):
        tablero[i]="-"
jugar()