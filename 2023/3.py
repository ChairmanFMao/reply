r = open("3input.txt","r")
o = open("3output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

# This approach works but, it is way to slow for the last 2 cases
# This is kinda slow but it does work

test_cases = int(r.readline())

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def fill(flowers: set, grounds: list, groundptr: int, min_dist: int, n_grounds, n_flowers):
    if len(flowers) + len(grounds) - groundptr < n_flowers:
        return 0
    if len(flowers) == n_flowers:
        return 1

    for i in range(groundptr,len(grounds)):
        too_close = False
        for flower in flowers:
            if dist(*flower, *grounds[i]) < min_dist:
                too_close = True

        if too_close:
            continue
        
        flowers.add(grounds[i])
        if fill(flowers, grounds, i+1, min_dist, n_grounds, n_flowers):
            return 1
        flowers.remove(grounds[i])
    return 0


for t in range(test_cases):
    w, h, n_flowers, n_grounds = [int(i) for i in r.readline().split()]

    grounds = list()
    for _ in range(n_grounds):
        grounds.append(tuple(int(i) for i in r.readline().split()))

    for d in range(300, 0, -1):
        print(t,d)
        if fill(set(), grounds, 0, d, n_grounds, n_flowers):
            o.write(f"Case #{t+1}: {d}\n")
            break

r.close()
o.close()