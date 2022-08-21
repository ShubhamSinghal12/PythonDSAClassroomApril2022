strs = ["eat","tea","tan","ate","nat","bat"]

dga = {}
for st in strs:
    l = list(st)
    l.sort()
    s = "".join(l)
    if s in dga:
        dga.get(s).append(st)
    else:
        dga[s] = [st]
ans = []
for v in dga.values():
    ans.append(v)
print(ans)
