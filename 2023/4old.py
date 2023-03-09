r = open("4input.txt","r")
o = open("4output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

t = int(r.readline())

for testCase in range(1,t+1):
    print(testCase)
    n, c, q = [int(i) for i in r.readline().split()]
    minimum=[-1,-1,-1,-1, n*n]
    grid = [[" " for i in range(n)] for j in range(n)]
    for i in range(q):
        x, y, t = r.readline().split()
        x = int(x); y = int(y)
        grid[x][y] = t

    if testCase > 3:
        continue

    for i in range(n):
        print(i)
        for j in range(i,n):
            pos=dict()
            for k in range(n):
                for l in range(i,j+1):
                    if grid[k][l]==" ":
                        continue
                    pos[grid[k][l]]=k
                if len(pos)==c:
                    area = (k-min(pos.values())+1)*(j-i+1)
                    if area < minimum[-1]:
                        minimum=[min(pos.values()),i,k,j,area]

    
    k=""
    for i in minimum:
        k+=str(i) +" "
    o.write(f"Case #{testCase}: {k[:-1]}\n")

r.close()
o.close()
