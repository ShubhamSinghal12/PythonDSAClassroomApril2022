n = 7

row = 1
nsp1 = 0
nsp2 = n-2

while row <= n:
    csp = 1
    while csp <= nsp1:
        print(" ",end=" ")
        csp += 1
    
    print("*",end= " ")

    csp = 1
    while csp <= nsp2:
        print(" ",end=" ")
        csp += 1
    
    if row != n//2+1:
        print("*",end= " ")

    if row < n//2+1:
        nsp1+=1
        nsp2-=2
    else:
        nsp1 -= 1
        nsp2 += 2
    
    row += 1
    print()