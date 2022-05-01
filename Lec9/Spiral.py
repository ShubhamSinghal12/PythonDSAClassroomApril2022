ll = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

te = len(ll)*len(ll[0])
ce = 0

minc = 0
maxc = len(ll[0])-1
minr = 0
maxr = len(ll)-1

while te > ce:

    i = minc
    while i <= maxc and te > ce:
        print(ll[minr][i],end=" ")
        ce += 1
        i += 1
    minr += 1

    i = minr
    while i <= maxr and te > ce:
        print(ll[i][maxc],end = " ")
        ce += 1
        i += 1
    maxc -= 1

    i = maxc
    while i >= minc and te > ce:
        print(ll[maxr][i],end= " ")
        ce += 1
        i -= 1
    maxr -= 1

    i = maxr
    while i >= minr and te > ce:
        print(ll[i][minc],end = " ")
        ce += 1
        i -= 1
    minc += 1

print()