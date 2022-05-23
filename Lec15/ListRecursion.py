def display(l,i):
    if i == len(l):
        return
    else:
        print(l[i])
        display(l,i+1)


def search(l,i,ele):
    if i == len(l):
        return -1
    else:
        if l[i] == ele:
            return i
        else:
            return search(l,i+1,ele)

def lastsearch(l,i,ele,ans):
    if i == len(l):
        return ans
    else:
        if l[i] == ele:
            return lastsearch(l,i+1,ele,i)
        else:
            return lastsearch(l,i+1,ele,ans)

def lsearch(l,i,ele):
    if i == -1:
        return -1
    else:
        if l[i] == ele:
            return i
        else:
            return lsearch(l,i-1,ele)

def All(l,i,ele,ans):
    if i == len(l):
        return
    else:
        if l[i] == ele:
            ans.append(i)
        
        All(l,i+1,ele,ans)

def All1(l,i,ele):
    if i == len(l):
        return []
    else:
        ans = All1(l,i+1,ele)
        if l[i] == ele:
            ans.insert(0,i)
        return ans

l = [3,5,4,2,1,3,2,1,2]
a = []
print(All1(l,0,2))
# print(a)
