r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

for c in range(1,t+1):
    n, k, m = [int(i) for i in r.readline().split()]
    p = []
    s = []
    for i in range(n):
        temp1, temp2 = [int(j) for j in r.readline().split()]
        p.append(temp1)
        s.append(temp2)

    # Binary search with time
    lower = 0; upper = int(1e18); mid = 0
    while lower < upper-1:
        mid = (lower+upper) // 2
        # operations for one computer = (time - startup) * operations
        # We then sort this to get the most efficient computers
        efficiency = sorted([(mid-p[i])//s[i] for i in range(n)], reverse=True)
        total = 0
        for i in range(min(k,len(efficiency))):
            total += efficiency[i]
        
        if total >= m:
            upper = mid
        else:
            lower = mid

    o.write(f"Case #{c}: {upper}\n")