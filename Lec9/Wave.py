ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(ll)):
    if i%2 == 0:
        for j in ll[i]:
            print(j,end=" ")
    else:
        for j in range(len(ll[i])-1,-1,-1):
            print(ll[i][j],end = " ")

print()

for j in range(len(ll[0])):
    if j%2 == 0:
        for i in range(len(ll)):
            print(ll[i][j],end= " ")
    else:
        for i in range(len(ll)-1,-1,-1):
            print(ll[i][j],end= " ")


print()