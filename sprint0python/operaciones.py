def add(addend1, addend2):
    return addend1 + addend2

def subtract(minuend, subtrahend):
    return minuend - subtrahend

def multiply(multiplicand, multiplier):
    return multiplicand*multiplier

def divide(dividend, divisor):
    if divisor == 0:
        print("El divisor no puede ser 0, se devolvera un 0")
        return 0
    else:
        return dividend / divisor
    