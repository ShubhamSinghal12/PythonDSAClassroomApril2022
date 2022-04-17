num = 57

multi = 1
ans = 0
base = 8

while num!=0:
    ans += (num%base)*multi

    multi *= 10
    num //= base

print(ans)
