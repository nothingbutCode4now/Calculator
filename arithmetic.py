print('''What operation do you wish to perform
Enter 1 for Addition
2.Subtraction
3.multiplication
4.Division
5.Modula
''')
def addition(a,b):
    print('Enter input')
    print(f'sum is {a+b}')
def subtraction(a,b):
    print('Enter input')
    print(f'difference is {a-b}')
def multiplication(a,b):
    print('Enter input')
    print(f'product is {a*b}')
def Division(a,b):
    print('Enter input')
    print(f'quotient is {a/b}')
def Modula(a,b):
    print('Enter input')
    print(f'modula is {a%b}')
x=input('Enter your choice')
if x=='1':
    addition(a,b)
elif x=='2':
    subtraction(a,b)
elif x=='3':
    multiplication(a,b)
elif x=='4':
    Division(a,b)
elif x=='5':
    Modula(a,b)
else:
    print('Not a valid input')
