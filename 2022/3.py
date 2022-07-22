r = open("./3input.txt","r")
o = open("./3output.txt","w")

t = int(r.readline())

# Not sure where the problem is, solution should be fast enough

for c in range(1,t+1):
    rows, columns, n, s, d, h = [int(i) for i in r.readline().split()]
    enemies = [[int(i) for i in r.readline().split()] for j in range(n)]
    # Sorts the enemies in the order of their y value from smallest to biggest
    enemies.sort(key=lambda x: x[3])

    # Stores all of the enemies in each row
    rowState = [[] for i in range(rows)]
    for i in enemies:
        rowState[i[2]].append(i[1])
    
    enemyCount = n; shots = 0
    # Loops through turns until the game is finished
    while enemyCount:
        rowPtr = 0
        counter = 0
        # Used because a for loop can't alter i
        while counter < s and enemyCount:
            # If there is an enemy in the row we hit it
            if len(rowState[rowPtr]):
                new = []
                # Reduces the hp of all the enemies in a row
                for i in range(len(rowState[rowPtr])):
                    rowState[rowPtr][i] -= max(0, d - (rowPtr * h))
                    # If the enemy has less than or 0 hp it is removed
                    if rowState[rowPtr][i] > 0:
                        new.append(rowState[rowPtr][i])
                enemyCount -= len(rowState[rowPtr]) - len(new)
                rowState[rowPtr] = new
                counter += 1
                shots += 1
            # Otherwise move across to the next row
            else:
                rowPtr += 1
        # Rotates the rows around
        rowState.append(rowState.pop(0))

    o.write(f"Case #{c}: {shots}\n")

r.close()
o.close()