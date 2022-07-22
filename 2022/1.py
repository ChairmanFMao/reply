import math

r = open("./1input.txt","r")
o = open("./1output.txt","w")

t = int(r.readline())



# brilliantly written code that gets a list of all prime numbers that could go into a value
def primelist(maxval):
  primelist = []
  maxprime = int(maxval) + 1
  
  thelist = []
  for i in range(2, maxprime+1):
    thelist.append(i)
  
  templist = []
  current = 0

  while int(current) < int(math.sqrt(maxprime)):

    try:
      current = thelist[0]
      doloop = True
    except:
      current = int(math.sqrt(maxprime)) + 1
      doloop = False

    if doloop == True:
      primelist.append(current)
      thelist.pop(0)
      
      
      for j in thelist:
        if j % current != 0:
          templist.append(j)
  
      thelist = templist[:]
      templist = []

  for i in thelist:
    primelist.append(i)

  return primelist





for c in range(1,t+1):


    (n, m) = r.readline().split(" ")  # get 2nd line here
    n = int(n)
    m = int(m)

    thirdline = r.readline().split(" ") # get third line here
    thirdlineint = []
    for k in thirdline:
        thirdlineint.append(int(k))


    plist = []
    for i in thirdlineint:
        plist.append(i)


    listofprimes = primelist(max(plist))
    howmanyofeach = []

    for i in listofprimes:
        howmanyofeach.append(0)

    for each in plist:
        factors = []
        numberof = []
        while each > 1:
            for i in listofprimes:
                if each % i == 0:
                    if i in factors:
                        numberof[factors.index(i)] += 2
                    else:
                        factors.append(i)
                        numberof.append(1)
                    each = each/i

        # once we have divided it by every prime
        for number in factors:
            if numberof[factors.index(number)] > howmanyofeach[listofprimes.index(number)]:
                howmanyofeach[listofprimes.index(number)] = numberof[factors.index(number)]

    lowestcommonmultiple = 1

    count = 0
    for i in howmanyofeach:
        if i > 0:
            lowestcommonmultiple = lowestcommonmultiple * (listofprimes[count] ** i)
        
        count += 1


    output = 1 + (m-1)//lowestcommonmultiple


    o.write(f"Case #{c}: {output}\n")

r.close()
o.close()