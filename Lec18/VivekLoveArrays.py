def vlag(arr):
    ts = sum(arr)
    if ts%2 == 1:
        return 0
    else:
        s = 0
        for i in range(len(arr)):
            s += arr[i]
            if s == ts//2:
                return 1+max(vlag(arr[:i+1]),vlag(arr[i+1:]))
        return 0

c = vlag([4,1,0,1,1,0,1])
print(c)