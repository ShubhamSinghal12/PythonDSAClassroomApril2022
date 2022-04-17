num = 71

multi = 1
ans = 0
base = 8

while num!=0:
    ans += (num%10)*multi

    multi *= base
    num //= 10

print(ans)
