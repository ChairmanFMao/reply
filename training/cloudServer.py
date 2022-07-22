#freddie has hoes

# i as startpoint, j as length of iteration

#input and output

#function to determine whether sum is greater than P value

#store last minimum value of sum greater than P value

# There needs to be a better algorithm - O(n^2) doesn't work fast enough
# We could binary search the length     

r = open("./input.txt","r")
o = open("./out.txt","w")

t = int(r.readline())

for c in range(1,t+1):
    n, p = [int(i) for i in r.readline().split()]
    cp = [int(i) for i in r.readline().split()]
    # This is an incremental sum array
    subtotal = 0
    preCalc = [0]
    for i in range(n):
        subtotal += cp[i]
        preCalc.append(subtotal)

    lower = 0; upper = 0; best = 1e9
    
    # Iterates over starting points
    for j in range(n):
        # Binary search the length
        bottom = j; top = n; mid = 0
        while bottom < top - 1:
            mid = (bottom + top) // 2
            if preCalc[mid] - preCalc[j] >= p:
                top = mid
            else:
                bottom = mid
        
        if preCalc[top] - preCalc[j] < best and preCalc[top] - preCalc[j] >= p:
            best = preCalc[top] - preCalc[j]
            lower = j
            upper = top-1

        # Iterates over lengths
        # for i in range(1,n+1):
        #     if j+i > n:
        #         break
        #     # Checks if the total is greater than or equal to p and if it is better
        #     if preCalc[j+i] - preCalc[j] >= p and preCalc[j+i] - preCalc[j] < best:
        #         best = preCalc[j+i] - preCalc[j]
        #         lower = j
        #         upper = j+i-1
        #     # This exits prematurely if the sum is already greater or equal to p
        #     elif preCalc[j+i] - preCalc[j] >= p:
        #         break
    
    o.write(f"Case #{c}: {lower} {upper}\n")