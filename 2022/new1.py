from math import gcd

r = open("1input.txt","r")
o = open("1output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)


t = int(r.readline())

for caseNumber in range(1,t+1):
    n, m = [int(i) for i in r.readline().split()]
    p = [int(i) for i in r.readline().split()]

    m -= 1

    tmp = p[0]
    for i in p:
        tmp = (tmp*i)//gcd(tmp,i)

    out = m//tmp + 1

    o.write(f"Case #{caseNumber}: {out}\n")


r.close()
o.close()
