
select = -1
while select == -1:
    try:
        select = int(input('''
        Calculator Program by Thomas Gozalie
        Choose a program by inputting a number:
            1: Simple eval calculator
            2: Calculator with functions
            3: Fibonacci up to nth number
            4: Prime number checker
    '''))
    except:
        print("\nInvalid input.")

def evalCalc(): print(float(eval(str(input("Enter formula to be calculated: ")))))


def addition(x,y): return x + y
def subtraction(x,y): return x - y
def mult(x,y): return x * y
def divide(x,y): return x / y
def power(x,y): return x ** y

def calculator():
    stored = 0
    for i in range(9999):
        sel = input(f'''\n   Functional Calculator (+, -, *, /, ^)          Current value: {stored}        
        ------------------------------------------
    Enter a symbol for operation, and the number (Example: '+ 3'): ''').split()
        if sel == "?":
            break
        if sel[0] == "+":
            stored = addition(stored, float(sel[1]))
        elif sel[0] == "-":
            stored = subtraction(stored, float(sel[1]))
        elif sel[0] == "*":
            stored = mult(stored, float(sel[1]))
        elif sel[0] == "/":
            stored = divide(stored, float(sel[1]))
        elif sel[0] == "^":
            stored = power(stored, float(sel[1]))
    return 0

    

def Fibonacci():
    n = int(input('''Print Fibonacci sequence up to nth number.
    Select n: '''))
    seqn = [1,1]
    if n > 2:
        for i in range(n+1):
            seqn.append(seqn[i]+seqn[i+1])
        print(seqn)

def primeCheck():
    n = int(input(''' Prime number checker
    Enter a number: '''))
    for i in range(2,n):
        if n%i == 0:
            print(f"{n} is not a prime number.")
            return 0
    print(f"{n} is a prime number.")



def selections(x):

    if x == 1:
        evalCalc()

    elif x == 2:
        calculator()

    elif x == 3:
        Fibonacci()

    elif x == 4:
        primeCheck()


selections(select)