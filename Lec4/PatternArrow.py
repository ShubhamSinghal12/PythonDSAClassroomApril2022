n = 5

row = 1
nsp1 = n-1
nst = 1
nsp2 = -1
val = 1
while row <= n:
    csp = 1
    while csp <= nsp1:
        print(" ",end=" ")
        csp += 1
    
    cst = 1
    cval = val
    while cst <= nst:
        print(cval,end= " ")
        cst += 1
        cval -= 1

    csp = 1
    while csp <= nsp2:
        print(" ",end=" ")
        csp += 1
    
    cst = 1
    cval += 1
    while cst <= nst and row > 1 and row < n:
        print(cval,end= " ")
        cst += 1
        cval += 1
    
    if row < n//2+1:
        nsp1 -= 2
        nsp2 += 2
        nst += 1
        val += 1
    else:
        nsp1 += 2
        nsp2 -= 2
        nst -= 1
        val -= 1

    row += 1
    print()

