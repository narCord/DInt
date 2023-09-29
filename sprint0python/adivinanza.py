import random

guessDictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

riddleList = ["Tengo agujas y no se coser, tengo numeros y no se leer\na. Una lechuga       b. Un reloj         c. Una zebra",
              "Te la digo y no me entiendes, te la repito y no me comprendes\na. Un buho           b. Un loro          c. Una tela",
              "Cuando llueve y sale el sol, todos los colores los tengo yo\na. El arcoiris       b. Una abeja        c. Un elefante"]

def randomNumber(minLimit, maxLimit):
    return random.randint(minLimit, maxLimit)

randomizedRiddleList = random.sample(riddleList, k = 3)

print (randomizedRiddleList[1])

#choice = input(">").lower()

#if guessDictionary[choice] == numberToGuess:
#    print("Acierto!\n")
#    points = 10
#else:
#    print("Erorr!\n")
#    points = -5

#print("Has obtenido "+str(totalPoints)+" puntos en total")
