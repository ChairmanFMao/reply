r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

for c in range(1,t+1):
    n, l = [int(i) for i in r.readline().split()]
    # Takes in all of the logs
    lines = []
    for i in range(l):
        lines.append([int(j) for j in r.readline().split()])
    
    # This will hold the score, penalty time then id
    teams = [[0, 0, i] for i in range(1,n+1)]
    used = [[[0 for i in range(5)] for j in range(5)] for k in range(n)]

    # Processes all of the logs individually
    for i in lines:
        if i[-1] and not used[i[1]-1][i[2]-1][i[3]-1]:
            used[i[1]-1][i[2]-1][i[3]-1] = 1
            teams[i[1]-1][1] -= i[0]
            teams[i[1]-1][0] += (i[3] * 100)

    # Times the team id by -1 to sort in increasing team order
    for i in range(n):
        teams[i][2] *= -1
    teams.sort(reverse=1)
    for i in range(n):
        teams[i][2] *= -1

    o.write(f"Case #{c}:")
    for i in teams:
        o.write(f" {i[2]}")
    o.write("\n")

r.close()
o.close()
