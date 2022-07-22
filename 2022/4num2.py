import itertools
# For each floor generate cost of getting each number of possible monsters. Someone else can do the rest.

r = open("./4input.txt","r")
o = open("./4output.txt","w")

t = int(r.readline())


def floorskip(floor, moves = ""):
    
    # floor is list of in, out, monsters, size, level

    # 0,0 is top left so

    if floor[0][0] > floor[1][0]: # in to right of out
        moves += "L" * (floor[0][0] - floor[1][0])
    elif floor[0][0] < floor[1][0]:
        moves += "R" * (floor[1][0] - floor[0][0])

    if floor[0][1] > floor[1][1]: # in is below out
        moves += "U" * (floor[0][1] - floor[1][1])
    elif floor[0][1] < floor[1][1]:
        moves += "D" * (floor[1][1] - floor[0][1])

    return moves
    

def traverseWholeFloor(currentx, currenty, exitx, exity, gridSize):
    moves = ""
    enterx = currentx; entery = currenty
    while currentx > 0:
        moves += "L"
        currentx -= 1
        if (currentx == exitx and currenty == exity):
            moves += "LR"
            currentx -= 1
            currentx += 1
    while currenty > 0:
        moves += "R"
        currenty -= 1
        if (currentx == exitx and currenty == exity):
            moves += "LR"
            currenty -= 1
            currenty += 1
    
    for i in range(gridSize):
        for j in range(gridSize):
            currenty += 1 if i % 2 else -1
            moves += "U" if i % 2 else "D"
        moves += "R"
        currentx += 1
        if (currentx == exitx and currenty == exity) or (currentx == enterx and currenty == entery):
            moves += "LR"
            currentx -= 1
            currentx += 1
    
    while currentx > exitx:
        moves += "L"
        currentx -= 1
        if (currentx == enterx and currenty == entery):
            moves += "DU"
            currenty -= 1
            currenty += 1
    while currenty > exity:
        moves += "D"
        currenty -= 1
        if (currentx == enterx and currenty == entery):
            moves += "DU"
            currenty -= 1
            currenty += 1
    
    return moves


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for c in range(1,t+1):
    N, L, P = [int(i) for i in r.readline().split()]
    floor_densities = {}
    floors = {} # contains tuple 
    for i in range(N):
        floornum, floor_size, monster_level = [int(i) for i in r.readline().split()]

        floor = []
        for y in range(floor_size):
            line = [i for i in r.readline().split()]
            floor.append(line)

        # Iterate over all possible paths through monsters
        monsters = []
        enter = None
        out = None
        for y, row in enumerate(floor):
            for x, el in enumerate(row):
                if el == "M":
                    monsters.append((x, y))
                elif el == "I":
                    enter = (x, y)
                elif el == "O":
                    out = (x, y)
                    
        floors[floornum] = (enter, out, floor_size)
        monsters_on_floor = sum(1 for i in row for row in floor if i=="M")
        
        density = monsters_on_floor / (floor_size**2)

        # Find shortest path for each number of monsters on this level
        floor_densities[floornum] = density

    choice = max(floor_densities.items(), key=lambda item: item[1])[0]
    print(choice, floors)
    
    res = ""
    for i in range(N):
        if i == choice:
            res += traverseWholeFloor(floors[i][0][0], floors[i][0][1], floors[i][1][0], floors[i][1][1], floors[i][2])
        else:
            res += floorskip(floors[i])

    o.write(f"Case #{c}: {res}\n")

o.close()
r.close()