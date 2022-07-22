r = open("./4input.txt","r")
o = open("./4output.txt","w")

t = int(r.readline())

for c in range(1,t+1):
    N, L, P = [int(i) for i in r.readline().split()]
    floors = []
    for i in range(N):
        floornum, size , level = [int(i) for i in r.readline().split()]
        din = [-1, -1]
        dout = [-1, -1]
        monsters = []
        for y in range(size):
            line = [i for i in r.readline().split()]
            for x in range(size):
                if(line[x] == "I"):
                    din[0] = x
                    din[1] = y

                if(line[x] == "O"):
                    dout[0] = x
                    dout[1] = y

                if(line[x] == "M"):
                    monsters.append([x, y])


        floors.append([din, dout, monsters, size, level])

    
    


        

    
    
    

    

         

    o.write(f"Case #{c}: {moves}\n")

r.close()
o.close()