from math import*

a = [pi, pi/2, 4*pi/3]

for x in a:
    if sin(x)**2 + cos(x)**2 == 1:
        print(f"Với x = {x}, biểu thức sin(x)**2 + cos(x)**2 == 1 là đúng")
    else:
        print(f"Với x = {x}, biểu thức sin(x)**2 + cos(x)**2 == 1 là sai")