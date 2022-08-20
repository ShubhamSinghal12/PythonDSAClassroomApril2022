l = [1,4,2,3,5,6,7]
df = set()
t = 10
for i in l:
    n = t-i
    if n in df:
        print(n,i)
    else:
        df.add(i)

