import random

guessDictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

def randomNumber(minLimit, maxLimit):
    return random.randint(minLimit, maxLimit)

def choiceGame(number):
    numberToGuess = randomNumber(1, 3)
    #print(numberToGuess)

    print("Adivinanza "+str(number)+": \"a\", \"b\" o \"c\"?")
    choice = input(">").lower()

    if guessDictionary[choice] == numberToGuess:
        print("Acierto!\n")
        points = 10
    else:
        print("Erorr!\n")
        points = -5
    
    return points

totalPoints = 0
totalPoints += choiceGame(1)
totalPoints += choiceGame(2)
totalPoints += choiceGame(3)

print("Has obtenido "+str(totalPoints)+" puntos en total")