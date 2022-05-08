l1 = [1,1,2,2,2,3,3,4,5,5,6,7,7,7,8]
l2 = [1,2,2,2,2,3,5,7,9,9,9,10,10]

i = 0
j = 0
ans = []

while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
        ans.append(l1[i])

        i+=1
        j+=1
    elif l1[i] < l2[j]:
        i += 1
    else:
        j += 1

print(ans)
