import math
import sys
x = int(input('Enter first number'))
y = int(input('Enter second number'))
z = int(input('Enter third number'))
a = x+y+z
print(a)

if x>y and x>z :
    print(x)
elif y>x and y>z :
        print(y)
else :
            print(z)