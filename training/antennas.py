from copy import deepcopy

r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

# Somehow getting wrong answer on the 4th test case after doing all the first 3

for p in range(t):
    n, k = [int(i) for i in r.readline().split()]
    a = sorted([int(i) for i in r.readline().split()])
    b = sorted([int(i) for i in r.readline().split()])
    abig = deepcopy(a); bbig = deepcopy(b)
    
    biggest = 0; smallest = 0;
    # Calculates the biggest possible
    for i in range(k):
        if abig[0] * bbig[0] > abig[-1] * bbig[-1]:
            biggest += abig[0] * bbig[0]
            abig.pop(0)
            bbig.pop(0)
        else:
            biggest += abig[-1] * bbig[-1]
            abig.pop()
            bbig.pop()
    
    # Calculates the smallest possible
    for i in range(k):
        if a[0] >= 0 and b[0] >= 0:
            if a[0] * b[k-i-1] < a[k-i-1] * b[0]:
                smallest += a[0] * b[k-i-1]
                a.pop(0)
                b.pop(k-i-1)
            else:
                smallest += a[k-i-1] * b[0]
                a.pop(k-i-1)
                b.pop(0)
        else:
            if a[0] * b[-1] > b[0] * a[-1]:
                smallest += b[0] * a[-1]
                a.pop()
                b.pop(0)
            else:
                smallest += a[0] * b[-1]
                a.pop(0)
                b.pop()
    
    o.write(f"Case #{p+1}: {smallest} {biggest}\n")