r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

# Unsure where the error is, works for first but not second
# Finish off tomorrow, I might ask for help from Zoran or Bredan idk.

for c in range(t):
    n, k = [int(i) for i in r.readline().split()]
    p = [int(i) for i in r.readline().split()]
    next = [0 for i in range(n)]
    used = [0 for i in range(n)]

    for i in range(n):
        if not used[i]:
            used[i] = 1
            around = [i]
            current = p[i]
            while current != i:
                around.append(current)
                used[current] = 1
                current = p[current]
            
            for j in range(len(around)):
                next[around[(k + j) % len(around)]] = around[j]
    
    o.write(f"Case #{c+1}:")
    for i in next:
        o.write(f" {i}")
    o.write("\n")
