from re import A
import random
#Tablero de juego
tablero =[  "-", "-", "-",
             "-", "-", "-",
              "-", "-", "-"]
#Variables de control
ganador = None
contador=1

#Ejecuta el juego
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
                    print("-------> LA MAQUINA HA GANADO EL TRIQUI B) <--------")
                    menu()
                break
        elif ganador=="X":
            print("-------> Felicadadesss!!! HAZ GANADO el TRIQUI :D <--------")
            menu()
            break
        else:
            print("-------> No hay ganador. El juego termina en EMPATE :/  <--------")
            menu()
#Muestra el menú para seguir jugando
def menu():
    aux=int(input('\nSi desea seguir jugando ingrese el 0 sino el 1: '))
    if (aux==0):
        vaciar()
        jugar()
    else:
        print('\n/////////////////////////  GRACIAS POR JUGAR  //////////////////////\n')
        exit(0)
#Determina si hay un ganador
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
#Realiza la jugada 
def jugada(valor,i):
    global contador
    anoto = False
    while anoto==False:
        if(i==48):
            posicion = int(input("Elegir una posicion del 1 al 9: "))
            posicion -= 1
        else:
            posicion=i
            
            
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("\n////////////////////////////")
            print("Esa posicion ya esta ocupada")
            print("////////////////////////////\n")
            i=48
            contador-=20
            ver_tablero()
    tablero[posicion] = valor
    ver_tablero()
#Realiza la jugada del computador
def juega_maquina():
    global contador
    anoto = False
    juego=""
    regla="si"
    while anoto==False:   
        aux=2
        if(tablero[0]=='X'):
            if(tablero[1]=='X')&(tablero[2]!='O'):
                posicion=3
                aux=0
            if(tablero[2]=='X')&(tablero[1]!='O'):
                posicion=2
                aux=0
            if(tablero[3]=='X')&(tablero[6]!='O'):
                posicion=7
                aux=0
            if(tablero[6]=='X')&(tablero[3]!='O'):
                posicion=4
                aux=0
        if(tablero[6]=='X'):
            if(tablero[3]=='X')&(tablero[0]!='O'):
                posicion=1
                aux=0
            if(tablero[0]=='X')&(tablero[3]!='O'):
                posicion=4
                aux=0
            if(tablero[7]=='X')&(tablero[8]!='O'):
                posicion=9
                aux=0
            if(tablero[8]=='X')&(tablero[7]!='O'):
                posicion=8
                aux=0
        if(tablero[8]=='X'):
            if(tablero[5]=='X')&(tablero[2]!='O'):
                posicion=3
                aux=0
            if(tablero[2]=='X')&(tablero[5]!='O'):
                posicion=6
                aux=0
            if(tablero[7]=='X')&(tablero[6]!='O'):
                posicion=7
            if(tablero[6]=='X')&(tablero[7]!='O'):
                posicion=8
                aux=0
        if(tablero[2]=='X'):
            if(tablero[1]=='X')&(tablero[0]!='O'):
                posicion=1
                aux=0
            if(tablero[0]=='X')&(tablero[1]!='O'):
                posicion=2
                aux=0
            if(tablero[5]=='X')&(tablero[8]!='O'):
                posicion=9
                aux=0
            if(tablero[8]=='X')&(tablero[5]!='O'):
                posicion=6
                aux=0
        if(tablero[4]=='X'):
            if(tablero[0]=='X')&(tablero[8]!='O'):
                posicion=9
                aux=0
            if(tablero[2]=='X')&(tablero[6]!='O'):
                posicion=7
                aux=0
            if(tablero[6]=='X')&(tablero[2]!='O'):
                posicion=3
                aux=0
            if(tablero[8]=='X')&(tablero[0]!='O'):
                posicion=1
                aux=0

            if(tablero[1]=='X')&(tablero[7]!='O'):
                posicion=8
                aux=0
            if(tablero[3]=='X')&(tablero[5]!='O'):
                posicion=6
                aux=0
            if(tablero[5]=='X')&(tablero[3]!='O'):
                posicion=4
                aux=0
            if(tablero[8]=='X')&(tablero[1]!='O'):
                posicion=2
                aux=0

        if(aux!=0):
            juego="seguro"
        else:
            juego="INSEGURO"

        if(juego=="seguro")&(regla=="si"):
            if(tablero[4]=='-'):
                posicion=5
                aux=1
            else:
                if(tablero[0]=='O'):
                    if(tablero[1]=='O'):
                        posicion=3
                        aux=1
                    if(tablero[2]=='O'):
                        posicion=2
                        aux=1
                    if(tablero[3]=='O'):
                        posicion=7
                        aux=1
                    if(tablero[6]=='O'):
                        posicion=4
                        aux=1
                if(tablero[6]=='O'):
                    if(tablero[3]=='O'):
                        posicion=1
                        aux=1
                    if(tablero[0]=='O'):
                        posicion=4
                        aux=1
                    if(tablero[7]=='O'):
                        posicion=9
                        aux=1
                    if(tablero[8]=='O'):
                        posicion=8
                        aux=1
                if(tablero[8]=='O'):
                    if(tablero[5]=='O'):
                        posicion=3
                        aux=1
                    if(tablero[2]=='O'):
                        posicion=6
                        aux=1
                    if(tablero[7]=='O'):
                        posicion=7
                        aux=1
                    if(tablero[6]=='O'):
                        posicion=8
                        aux=1
                if(tablero[2]=='O'):
                    if(tablero[1]=='O'):
                        posicion=1
                        aux=1
                    if(tablero[0]=='O'):
                        posicion=2
                        aux=1
                    if(tablero[5]=='O'):
                        posicion=9
                        aux=1
                    if(tablero[8]=='O'):
                        posicion=6
                        aux=1
                if(tablero[4]=='O'):
                    if(tablero[6]=='O'):
                        posicion=3
                        aux=1
                    if(tablero[8]=='O'):
                        posicion=1
                        aux=1
                    if(tablero[0]=='O'):
                        posicion=9
                        aux=1
                    if(tablero[2]=='O'):
                        posicion=7
                        aux=1
                
        if(regla=="no")&(contador>3):
            posicion=random.randrange(0,9) 
        if(regla=="si")&(contador<3)&(tablero[4]!='-'):
            a,aux=claves()
            if(aux!=3):
                posicion=random.randrange(0,9)  
                
                
        try:        
            posicion-=1 
        except:
            posicion,aux=claves()
            print(posicion)
         
        if tablero[posicion] == "-":
            anoto = True
        
        else:
            anoto= False
            regla="no"
    contador +=1
    aux=0
    return posicion
    
#Difine las jugadas de libro
def claves():
    posicion=0
    aux=1
    if(tablero[8]=='X'):
        if(tablero[3]=='X'):
            posicion=7
            posicion-=1 
            aux=3
        elif(tablero[1]=='X'):
            posicion=3
            posicion-=1
            aux=3
    if(tablero[6]=='X'):
        if(tablero[1]=='X'):
            posicion=1
            posicion-=1 
            aux=3
        elif(tablero[5]=='X'):
            posicion=7
            posicion-=1 
            aux=3
    if(tablero[0]=='X'):
        if(tablero[7]=='X'):
            posicion=4
            posicion-=1 
            aux=3
        elif(tablero[5]=='X'):
            posicion=3
            posicion-=1 
            aux=3
    if(tablero[2]=='X'):
        if(tablero[7]=='X'):
            posicion=4
            posicion-=1 
            aux=3
        elif(tablero[3]=='X'):
            posicion=1
            posicion-=1 
            aux=3
    return posicion,aux
#Muestra el tablero de juego
def ver_tablero():
    print("\n")
    print("\t                                  \t                          ",tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print("\t                                  \t                          ",tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print("\t                                  \t                          ",tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print("\n")
#Limpia el juego para un nuevo inicio
def vaciar():
    global ganador
    ganador=None
    for i in range(9):
        tablero[i]="-"

jugar()