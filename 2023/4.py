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

    # This does the preprocessing 
    dp = [[dict() for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in dp[i-1][j].keys():
                if dp[i][j].get(k) == None:
                    dp[i][j][k] = 0
                dp[i][j][k] += dp[i-1][j][k]
            for k in dp[i][j-1].keys():
                if dp[i][j].get(k) == None:
                    dp[i][j][k] = 0
                dp[i][j][k] += dp[i][j-1][k]
            for k in dp[i-1][j-1].keys():
                if dp[i][j].get(k) == None:
                    dp[i][j][k] = 0
                dp[i][j][k] -= dp[i-1][j-1][k]
            if grid[i-1][j-1] != " ":
                if dp[i][j].get(grid[i-1][j-1]) == None:
                    dp[i][j][grid[i-1][j-1]] = 0
                dp[i][j][grid[i-1][j-1]] += 1
    
    total = len(dp[n][n])

    # This iterates over the starting point
    for i in range(1,n+1):
        print("first",i)
        for j in range(1,n+1):
            # This iterates over where it goes down to
            for k in range(i+1,n+1):
                # Now we do a binary search here
                lower = j+1; upper = n; mid = 0; pl = -1; pu = 0; valid = 0
                while lower <= upper:
                    if lower == pl and upper == pu:
                        break

                    mid = (lower+upper)//2
                    d = dict()
                    # subtract these
                    for l in dp[k][j-1].keys():
                        if d.get(l) == None:
                            d[l] = 0
                        d[l] -= dp[k][j-1][l]
                    for l in dp[i-1][mid].keys():
                        if d.get(l) == None:
                            d[l] = 0
                        d[l] -= dp[i-1][mid][l]
                    # add these
                    for l in dp[i-1][j-1].keys():
                        if d.get(l) == None:
                            d[l] = 0
                        d[l] += dp[i-1][j-1][l]
                    for l in dp[k][mid].keys():
                        if d.get(l) == None:
                            d[l] = 0
                        d[l] += dp[k][mid][l]

                    current = 0
                    for l in d.keys():
                        if d[l] > 0:
                            current += 1
                    
                    pl = lower; pu = upper
                    if current < total:
                        lower = mid
                    else:
                        upper = mid
                        valid = 1
                
                if valid:
                    area = (k-i)*(upper-j+1)
                    if area < minimum[-1]:
                        minimum = [i,j,k,upper,area]
                    
    
    k=""
    for i in minimum:
        k+=str(i) +" "
    o.write(f"Case #{testCase}: {k[:-1]}\n")

r.close()
o.close()
