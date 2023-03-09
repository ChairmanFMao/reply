r = open("5input.txt","r")
o = open("5output2.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

def count_seen(row: list, height: int):
    max_height = height
    dist = 0
    for house_height in row:
        if house_height <= max_height:
            continue
        dist += 1
        
        max_height = max(max_height, house_height)
    return dist


def generate(board, size, N, E, S, W, neighbours):
    """
    Generate valid result boards given the initial configuration info.

    board is a flat list containing the current board row by row

    each number contains the height of the building
    """

    rowi, coli = divmod(len(board), size)
    row = board[rowi * size : rowi * size + size]
    col = board[coli::size]

    if len(board) == size * size:
        # East constraint for final row
        incorrect = False
        last_row = board[(rowi) * size : (rowi) * size + size]
        for house_col, house_height in enumerate(last_row):
            myrow = last_row[house_col+1:]

            if count_seen(myrow, house_height) != E[rowi - 1][house_col]:
                incorrect = True

        if incorrect:
            return
            
        # South constraint for every column
        for col_i in range(size):
            col = board[col_i::size]
            for house_row, house_height in enumerate(col):
                mycol = col[house_row+1:]

                if count_seen(mycol, house_height) != S[house_row][col_i]:
                    incorrect = True

        if incorrect:
            return
            
        # Check neighbour constraint
        valid=True
        for i,j in enumerate(board):
            n=0
            for k in range(-1,2):
                for l in range(-1,2):
                    y,x=k+i//size,l+i%size
                    if not (0<=x<size and 0<=y<size):
                        continue
                    newpos=size*y+x
                    if board[newpos]>j:
                        n+=1
            if not n==neighbours[i//size][i%size]:
                #print(i, n, neighbours[i//size][i%size], neighbours, board)
                valid=False
                break
            
        if not valid:
            return
        
        yield board
        return

    for height in range(0, 100): #GOOD JOB LADS
        # Doesn't exist on column
        if height in row:
            continue

        # Doesn't exist in row
        if height in col:
            continue

        # North constraint
        if count_seen(col[::-1], height) != N[rowi][coli]:
            continue

        # West constraint
        if count_seen(row[::-1], height) != W[rowi][coli]:
            continue

        # If row complete
        incorrect = False
        if coli == 0 and rowi > 0:
            # East constraint for houses on previous row
            last_row = board[(rowi-1) * size : (rowi-1) * size + size]
            for house_col, house_height in enumerate(last_row):
                myrow = last_row[house_col+1:]

                if count_seen(myrow, house_height) != E[rowi - 1][house_col]:
                    incorrect = True

        if incorrect:
            break

        yield from generate([*board, height], size, N, E, S, W, neighbours)


t = int(r.readline())
for case_number in range(t):
    n = int(r.readline())

    r.readline()

    N = []
    for i in range(n):
        N.append([int(x) for x in r.readline().split()])

    S = []
    r.readline()
    for i in range(n):
        S.append([int(x) for x in r.readline().split()])
    r.readline()
    W = []
    for i in range(n):
        W.append([int(x) for x in r.readline().split()])
    r.readline()
    E = []
    for i in range(n):
        E.append([int(x) for x in r.readline().split()])

    neighbours = []
    r.readline()
    for i in range(n):
        neighbours.append([int(x) for x in r.readline().strip().split(" ")])

    #second = False
    for soln in generate([], n, N, E, S, W, neighbours):
        # !!! DO NOT ASK HOW THIS WORKS !!! how does it work?
        #if second:
        #    print("OH NO")
        answer = "\n".join(" ".join(map(str, yeet)) for yeet in zip(*[iter(soln)]*n))
        print(answer)
        o.write(f"Case #{case_number+1}:\n{answer}\n")
        #second = True
        break

r.close()
o.close()
