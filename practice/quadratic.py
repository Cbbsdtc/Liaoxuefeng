import math

def quadratic(a, b, c):
    delta = b*b-4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2/a
        x2 = (-b - math.sqrt(delta))/2/a
        print("此函数有两个根"+"x1="+str(x1)+', '+"x2="+str(x2))

quadratic(2,3,1)
quadratic(1,3,-4)






