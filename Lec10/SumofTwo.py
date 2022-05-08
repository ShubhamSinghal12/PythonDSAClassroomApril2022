l1 = [1,0,2,4]
l2 = [9,9,6,7,8]

l3 = []

i = len(l1)-1
j = len(l2)-1
c = 0
while i >= 0 or j >= 0:
    sum = c
    if i >= 0:
        sum += l1[i]
        i -= 1

    if j >= 0:
        sum += l2[j]
        j -= 1
    
    l3.insert(0,sum%10)
    c = sum//10

if c > 0:
    l3.insert(0,c)

# l3.reverse()
print(l3)