import random

guessDictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

def randomNumber(minLimit, maxLimit):
    return random.randint(minLimit, maxLimit)

numberToGuess = randomNumber(1, 3)
#print(numberToGuess)

print("Opcion \"a\", \"b\" o \"c\"?")
choice = input(">").lower()

if guessDictionary[choice] == numberToGuess:
    print("Acierto!")
else:
    print("Erorr!")