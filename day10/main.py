def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {"+": add, "-":subtract, "*": multiply, "/":division}

option = ''

while True:
    if not option == 'y':
        n1 = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    operation = input("Pick a operation: ")
    n2 = float(input("What's the next number?: "))

    if option == 'y':
        n1 = result      
    result = operations[operation]


    print(f"{n1} {operation} {n2} = {result}")
    option = input(f"type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 'x' for exit: ")


