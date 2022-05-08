def isVowel(st):
    return st in "aeiou"

def pwgs(st):
    ct = 0
    maxct = 0
    for i in range(len(st)):
        if isVowel(st[i]):
            ct += 1
        else:
            ct = 0

        if maxct < ct:
            maxct = ct
    
    return maxct

print(pwgs("aecbaeicbe"))