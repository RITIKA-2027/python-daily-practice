
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"
 
print(calculator(10, 5, "+"))   
print(calculator(10, 0, "/"))   
print(calculator(6, 7, "*"))   
    