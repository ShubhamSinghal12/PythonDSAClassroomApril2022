n = 100
num = 2
while num <= n:
    i = 2
    while i < num/2:
        # print("Hi")
        if num%i == 0:
            # print("Not Prime")
            break
        i += 1
    else:
        print(num,end = " ")
    
    num += 1
