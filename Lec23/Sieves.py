import math
def sieves(n):

    l = [True for i in range(n+1)]
    
    # for i in range(2,n):
    #     if l[i] == True:
    #         j=2
    #         while j*i <= n:
    #             l[i*j] = False
    #             j += 1

    x = int(math.sqrt(n))

    for i in range(2,x+1):
        if l[i] == True:
            # print(i)
            for j in range(i*i,n+1,i):
                l[j] = False
    
    for i in range(2,len(l)):
        if l[i]:
            print(i)

sieves(30)
    
