# def functions

def mult_fun(n1, n2):
    res = n1 * n2
    return res

def subtr_fun(n1, n2):
    res = n1 - n2
    return res
  
def add_fun(n1, n2):
    return n1 + n2

def div_fun(n1, n2):
    if n2 == 0:
        res = 'You cannot divide by Zero'
    else:
        res = n1 / n2
    return res


def main_fun(i):
    n1, operator, n2 = i.split()

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
    
    print(res)

input_ = input()
main_fun(input_)
