ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


for i in range(len(ll)-1):
    for j in range(i+1,len(ll[0])):
        t = ll[i][j]
        ll[i][j] = ll[j][i]
        ll[j][i] = t

for i in ll:
    print(i)