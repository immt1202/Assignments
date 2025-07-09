# Task 1

a=input('Enter the first number: ')
b=input('Enter the second number: ')
a=float(a)
b=float(b)
c1=a+b
c2=a-b
c3=a*b

if b != 0:
    c4 = a/b
else:
    c4 = None
print("Addition: ", int(c1))
print('Subtraction: ',int(c2))
print('Multiplication: ',int(c3))

if c4 is None:
    print('Division: Unidentified (Cannot divide by zero)')
else:
    print('Division',c4)



