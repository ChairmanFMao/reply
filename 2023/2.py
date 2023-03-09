r = open("2input.txt","r")
o = open("2output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

t = int(r.readline())

for testCase in range(1,t+1):
    n, total, money = [int(i) for i in r.readline().split()]
    machines = [[int(i) for i in r.readline().split()] for j in range(n)]

    machines.sort(key=lambda a:a[0])
    best = 0; ptr = 0; games = 0
    while ptr < len(machines) and machines[ptr][0] <= money:
        best = max(best,machines[ptr][1]-machines[ptr][0])
        ptr += 1
  
    while money < total:
        if ptr < len(machines):
            val = machines[ptr][0]
        else:
            val = total

        current = (val-money + best-1)//best
        games += current
        money += best * current

        while ptr < len(machines) and machines[ptr][0] <= money:
            best = max(best,machines[ptr][1]-machines[ptr][0])
            ptr += 1

    o.write(f"Case #{testCase}: {games}\n")

r.close()
o.close()
