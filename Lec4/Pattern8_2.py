n = 7

row = 1
nst = n

while row <= n:
    cst = 1
    while cst <= nst:
        if cst == row or cst+row == n+1:
            print("*",end=" ")
        else:
            print(" ",end= " ")
        cst += 1
    
    row+= 1
    print()