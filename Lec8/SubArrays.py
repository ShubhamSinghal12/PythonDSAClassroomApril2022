def subArrays(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            
            for k in range(i,j+1):
                print(l[k],end=" ")
            print()

def sumSubArrays(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            sum = 0
            for k in range(i,j+1):
                # print(l[k],end=" ")
                sum += l[k]
            print(sum)

def sumSubArrays2(l):
    for i in range(len(l)):
        sum = 0
        for j in range(i,len(l)):
            sum += l[j]

            print(sum)

def maxSumSubArrays(l):
    max = l[0]
    for i in range(len(l)):
        sum = 0
        for j in range(i,len(l)):
            sum += l[j]
            # print(sum)
            if max < sum:
                max = sum
    print(max)

def kadanesAlgo(l):
    sum = 0
    maxS = l[0]
    for i in range(len(l)):
        sum += l[i]
        if maxS < sum:
            maxS = sum
        if sum < 0:
            sum = 0
    print(maxS)

l = [1,-2,3,4,-5,6]
kadanesAlgo(l)