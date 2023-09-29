import random

riddleList = ["Tengo agujas y no se coser, tengo numeros y no se leer\na. Una lechuga       b. Un reloj         c. Una zebra",
              "Te la digo y no me entiendes, te la repito y no me comprendes\na. Un buho           b. Un loro          c. Una tela",
              "Cuando llueve y sale el sol, todos los colores los tengo yo\na. El arcoiris       b. Una abeja        c. Un elefante"]

def randomNumber(minLimit, maxLimit):
    return random.randint(minLimit, maxLimit)

def testAnswer(answer, randomRiddle):
    if(randomRiddle[4] == 'o' and answer == 'b'):
        print("Acierto")
        points = 10
    elif(randomRiddle[4] == 'a' and answer == 'c'):
        print("Acierto")
        points = 10
    elif(randomRiddle[4] == 'd' and answer == 'a'):
        print("Acierto")
        points = 10
    else:
        print("Error")
        points = -5
    return points

points = 0

#Randomizacion de los acertijos
randomizedRiddleList = random.sample(riddleList, k = 3)

#Primer acertijo
print(randomizedRiddleList[0])
choice = input(">").lower()
points += testAnswer(choice, randomizedRiddleList[0])

#Segundo acertijo
print(randomizedRiddleList[1])
choice = input(">").lower()
points += testAnswer(choice, randomizedRiddleList[1])

#Tercer acertijo
print(randomizedRiddleList[2])
choice = input(">").lower()
points += testAnswer(choice, randomizedRiddleList[2])

print("Has obtenido "+str(points)+" puntos en total")