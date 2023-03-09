import math
r = open("1input.txt","r")
o = open("1output.txt","w")

T=int(r.readline().strip())

for q in range(T):
    R,C=map(int, r.readline().strip().split())
    times=dict()
    for i in range(C):
        id,s,t,d,c=map(int, r.readline().strip().split())
        k=R//(t*c+s*d)
        time=k*(c+d)
        a=R%(t*c+s*d)
       # print(time)
        if a<=t*c:
      #      print(1,a/t)
            time+=math.ceil(a/t)
        else:
            time+=c
            a-=t*c
     #       print(2,a/s)
            time+=math.ceil(a/s)
        times[id]=time
    n=min(times.values())
    #print(times)
    for i in times:
        if times[i]==n:
            
            o.write(f"Case #{q+1}: {i}\n")
            break










r.close()
o.close()
