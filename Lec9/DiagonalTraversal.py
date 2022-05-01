ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

m = len(ll)
n = 0
for k in range(len(ll)+len(ll[0])-1):
    if k < len(ll):
        # i = len(ll)-1-k
        # j = 0
        m -= 1
    else:
        # i = 0
        # j = k-len(ll)+1
        n += 1
    
    i = m
    j = n
    while i < len(ll) and j < len(ll[0]):
        print(ll[i][j],end= " ")
        i += 1
        j += 1

    print()
