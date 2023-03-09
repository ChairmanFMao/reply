r = open("5input.txt","r")
o = open("5output.txt","w")

# To get input line by line do:
# r.readline()
#
# To output to the file do:
# o.write(...)

t = int(r.readline())
n = int(r.readline())

r.readline()

def rowheight(row): # first to last
    order=[]
    for i,j in row:
        order.insert()
    


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




r.close()
o.close()

