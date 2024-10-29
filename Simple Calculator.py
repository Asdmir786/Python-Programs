def SimpleCalculator(a,b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*" or operator == "x":
        return a*b
    elif operator == "÷" or operator == "/":
        return a/b
    elif operator == "^":
        return a**b
    

a = int(input("Gimme a Number\n: "))
operator = input("Gimme an operator like plus, etc...\n: ")
b = int(input("Gimme a Number Again\n: "))
print(SimpleCalculator(a,b,operator))
    