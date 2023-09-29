import operaciones
repeat = "s"

while repeat == "s":
    print("Introduce dos numeros con los que operar")
    firstNumber = int(input("Primer numero: "))
    secondNumber = int(input("Segundo numero: "))
    print("\nOperacion a realizar? ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    choice = int(input(">"))
    print("")

    if choice == 1:
        print(operaciones.add(firstNumber, secondNumber))
    elif choice == 2:
        print(operaciones.subtract(firstNumber, secondNumber))
    elif choice == 3:
        print(operaciones.multiply(firstNumber, secondNumber))
    elif choice == 4:
        print(operaciones.divide(firstNumber, secondNumber))

    print("\nRealizar otra operacion? S/n")
    repeat = input(">")