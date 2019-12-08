from math import *
import matplotlib.pyplot as plt
n = 0
xvalue = []
yvalue = []
print("Input the equation")
eq = input() 
def ncount(eq,n):
    return eval(eq)
while n <= 199:
    # sin((3*pi/100)*n) the equation used
    x = eval(eq)
    xvalue.append(x)
    if n == 0:
       y =  -1.5*ncount(eq,n) + 2*ncount(eq,n + 1) - 0.5*ncount(eq,n + 2)
       yvalue.append(y)
           
    if n <= 198:
        y = 0.5*ncount(eq,n + 1) - 0.5*ncount(eq,n - 1)
        yvalue.append(y)
             
    if n == 199:
        y =  1.5*ncount(eq,n) - 2*ncount(eq,n - 1) + 0.5*ncount(eq,n - 2)
        yvalue.append(y)
        
    n = n + 1
y1 = list(range(200))
plt.plot(y1,xvalue,label = "X function")
y2 = list(range(201))
plt.plot(y2,yvalue,label = "Y function")
plt.show
plt.legend()    