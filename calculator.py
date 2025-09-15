# def functions

def subtract(a, b):
return a - b



# main
n1, operator, n2 = input().split()

try:
    n1 = float(n1)
    n2 = float(n2)

    if operator == '+':
        res = add_fun(n1, n2) # Addition
        
    elif operator == '-':
        res = subtr_fun(n1, n2) # Subtraction
        
    elif operator == '*':
        res = mult_fun(n1, n2) # Multiplication
        
    elif operator == '/':
        res = div_fun(n1, n2) # Division - add condition for "Division by zero!"
    
    else:
        res = "Invalid arithmetic operator!"

except ValueError:
    res = "Enter the numbers!"

print(res)
