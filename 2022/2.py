r = open("./2input.txt","r")
o = open("./2output.txt","w")

t = int(r.readline())

def dist(p1, p2, ignore):
    # if ignore is aa just return the distance
    if ignore != "aa":
        # Otherwise try and demote some values
        
        # If the number left is 0 
        if p1[2] == 0:
            return 1e10
        # Don't return the current point again
        if p1 == p2:
            return 1e9

        # Don't return if the current point was the last point
        if p1 == p2 == ignore:
            return 1e8

    # Return the distance
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for c in range(1,t+1):
    N, M = [int(i) for i in r.readline().split()]

    targets = []
    for _ in range(M):
        tx, ty, tmax = [int(i) for i in r.readline().split()]
        targets.append([tx, ty, tmax])
    
    totdist = 0
    curr = targets[0]
    last = None
    while True:
        # Decrement the current target
        curr[2] -= 1

        # If the current target i is 0, remove it
        if curr[2] == 0:
            i = targets.index(curr)
            targets.pop(i)

        # This terminates if all the values are fully used up
        if all(i[2] == 0 for i in targets):
            break
        
        working = [a for a in targets if (a != curr and a != last) or len(targets) < 3]
        nxt = min(working, key=lambda p: (dist(p, curr, last), p[0], p[1]))
        totdist += dist(curr, nxt, "aa")

        last = curr
        curr = nxt

    o.write(f"Case #{c}: {totdist}")
    o.write("\n")

r.close()
o.close()