from essential import clear, logo

def add(n1, n2): return n1 + n2

def subtract(n1, n2): return n1 - n2

def multiply(n1, n2): return n1 * n2

def division(n1, n2): return n1 / n2

operations = {"+": add, "-":subtract, "*": multiply, "/":division}

clear()

def calculator():
    n1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick a operation: ")
        n2 = float(input("What's the next number?: "))    
        result = operations[operation_symbol](n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {result}")
        
        if input(f"type 'y' to continue calculating with {result}, type 'n' to start a new calculation: ") == 'y':
            n1 = result
        else:
            should_continue = False
            clear()
            print(logo)
            calculator()

print(logo)
calculator()

