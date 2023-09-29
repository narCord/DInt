import random

guessDictionary = {
    1: 'Piedra',
    2: 'Papel',
    3: 'Tijera'
}

repeat = 's'
while repeat == 's':
    round = 0
    score = 0

    while round < 5:
        #Jugada de la maquina
        machinePlay = random.randint(1, 3)

        #Jugada del jugador
        #print(machinePlay)
        playerPlay = 10
        while (playerPlay < 1 or playerPlay) > 3:
            print("1. Piedra        2. Papel        3.Tijera")
            playerPlay = int(input("Selecciona tu jugada: "))

        #Logica de decision del ganador
        if (playerPlay == machinePlay):
            print("Empate")
        elif (playerPlay == 1):
            if (machinePlay == 2):
                print("+1 Punto para la maquina")
                score -= 1
            else:
                print("+1 Punto para el jugador")
                score += 1
        elif (playerPlay == 2):
            if (machinePlay == 3):
                print("+1 Punto para la maquina")
                score -= 1
            else:
                print("+1 Punto para el jugador")
                score += 1
        elif (playerPlay == 3):
            if (machinePlay == 1):
                print("+1 Punto para la maquina")
                score -= 1
            else:
                print("+1 Punto para el jugador")
                score += 1

        round += 1
        print("\n")

    #Declaracion del ganador
    if (score > 2):
        print("Has ganado la partida!")
    else:
        print("La maquina ha ganado la partida...")
            
    repeat = input("Volver a jugar? S/n").lower()
