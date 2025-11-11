
import math

def square(a, b, c):
    if a == 0:
        x = - c / b
        return x
    
    else:
        dt = b*b - 4 *a *c
    if dt > 0:
        x1 = (-b + math.sqrt(dt)) / (2*a)
        x2 = (-b - math.sqrt(dt)) / (2*a)
        return (x1, x2)
    elif dt == 0:
        x = -b/(2*a)
        x = x1 = x2
        return(x1, x2)
    else: 
        print("pt vo nghiem")
        return None

print(square(1,4,3))