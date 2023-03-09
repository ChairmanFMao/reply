r = open("2input.txt","r")
o = open("2output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

# This is quite slow for bigger cases but it will work within the 2 mins just

t = int(r.readline())

for caseNumber in range(1,t+1):
    n, m = [int(i) for i in r.readline().split()]

    grid = [[0 for i in range(n)] for j in range(n)]
    out = 0; pos = [0,0]; tot = 0
    for i in range(m):
        x, y, val = [int(i) for i in r.readline().split()]
        if not i:
            pos = [x,y]
        tot += val
        grid[x][y] = val

    def close(x, y, past,left):
        best = 1000; p = [-1,-1]
        for i in range(n):
            for j in range(n):
                if (i == x and j == y) or (i == past[0] and j == past[1] and left > 2):
                    continue

                if abs(x-i) + abs(y-j) < best and grid[i][j]:
                    best = abs(x-i) + abs(y-j)
                    p = [i,j]
        
        return p

    tot -= 1
    grid[pos[0]][pos[1]] -= 1
    prev = pos

    def leftCalc():
        l = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    l += 1
        return l
    
    left = leftCalc()

    while tot:
        print(tot)
        nextPos = close(pos[0],pos[1],prev,left)
        if nextPos[0] == -1:
            break
        out += abs(pos[0]-nextPos[0]) + abs(pos[1]-nextPos[1])
        grid[nextPos[0]][nextPos[1]] -= 1
        prev = pos
        pos = nextPos
        left = leftCalc()

        tot -= 1

    
    o.write(f"Case #{caseNumber}: {out}\n")


r.close()
o.close()
