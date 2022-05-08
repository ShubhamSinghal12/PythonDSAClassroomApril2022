k = 5
l = [4,5,0,-2,-3,1]

def subarraysDivByK(nums, k):
    hole = [0 for i in range(k)]
    hole[0] = 1
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        hole[sum%k] += 1
    # print(hole)
    count = 0
    for i in hole:
        if i >= 2:
            count += i*(i-1)//2
    
    return count

print(subarraysDivByK(l,k))

