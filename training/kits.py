from math import gcd

r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

for p in range(t):
    n = int(r.readline())
    g = [int(i) for i in r.readline().split()]
    out = g[0]
    for i in range(1,len(g)):
        out = gcd(out, g[i])
    
    output = 1
    for i in range(2,out+1):
        current = 1
        while not out % i:
            out //= i
            current += 1
        output *= current
    
    o.write(f"Case #{p+1}: {output}\n")

o.close()
r.close()