r = open("./5input.txt","r")
o = open("./5output.txt","w")



t = int(r.readline())

# We could potentially brute force it considering the constraints are very small
# Number of distinct gaps is one of these: y-1, y, y+1

for c in range(1,t+1):

    # Checks if the current grid is valid
    def validate():
        # Iterates over all of the rows
        for i in range(n):
            # Sums up the number of gaps
            gaps = 0
            for j in range(n):
                gaps += grid[i][j]
            # Checks if the number of gaps is valid
            if gaps != n - xrow[i]:
                return 0
        
        # Iterates over all of the columns
        for i in range(n):
            # Sums up the number of gaps
            gaps = 0
            for j in range(n):
                gaps += grid[j][i]
            # Checks if the number of gaps is valid
            if gaps != n - xcol[i]:
                return 0

        return 1

    # Handles the inputs
    n, lmin, lmax = [int(i) for i in r.readline().split()]
    xcol, ycol, zcol = [[int(j) for j in r.readline().split()] for _ in range(3)]
    xrow, yrow, zrow = [[int(j) for j in r.readline().split()] for _ in range(3)]

    # Creates a grid of booleans
    grid = [[1 for i in range(n)] for j in range(n)]

    # This is the total number of ship squares
    totalShipSquares = sum(xcol)

    # This will brute force all of the gap combinations
    for i in range(n):
        # We know that there will be one gap of length zrow[i]
        gapsLeft = n - zrow[i] - xrow[i]
        possible = []
        # We need to make the number gapsLeft as the sum of i numbers
        for i in range(yrow[i]-1, yrow[i]+2):
            if i < 0 or i > n:
                break
            

    o.write(f"Case #{c}:")

r.close()
o.close()























def findCombinationsUtil(arr, index, num, reducedNum):
 
    # Base condition
    if (reducedNum < 0):
        return
 
    # If combination is
    # found, print it
    if (reducedNum == 0):
 
        for i in range(index):
            print(arr[i], end = " ")
        print("")
        return
 
    # Find the previous number stored in arr[].
    # It helps in maintaining increasing order
    prev = 1 if(index == 0) else arr[index - 1]
 
    # note loop starts from previous
    # number i.e. at array location
    # index - 1
    for k in range(prev, num + 1):
         
        # next element of array is k
        arr[index] = k
 
        # call recursively with
        # reduced number
        findCombinationsUtil(arr, index + 1, num, reducedNum - k)
 
# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def findCombinations(n):
     
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * n
 
    # find all combinations
    findCombinationsUtil(arr, 0, n, n)