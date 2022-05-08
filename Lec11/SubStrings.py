def subString(st):
    for i in range(len(st)):
        for j in range(i,len(st)):
            print(st[i:j+1])

def reverse1(st):
    s = ""
    for i in range(-1,-len(st)-1,-1):
        s += st[i]
    return s

def reverse2(st):

    return st[::-1]

def isPalindrome(st):
    return st == reverse2(st)

def isPalindrome2(st):
    si = 0
    ei = len(st)-1
    while si < ei:
        if st[si] != st[ei]:
            return False
        else:
            si += 1
            ei -= 1
    return True


def CountPalindromicSubString(st):
    count = 0
    for i in range(len(st)):
        for j in range(i,len(st)):
            if isPalindrome(st[i:j+1]):
                count += 1
    return count

def reverseWordbyWord(st):
    l = st.split()
    l.reverse()
    s = ""
    for i in l:
        s += i + " "
    return s
def rw_w(st):
    s = ""
    for i in range(len(st)-1,-1,-1):
        if st[i] == " ":
            s += st[i+1:len(st)]+" "
            st = st[:i]
    
    return s+st

print(rw_w("The Sky is Blue"))
# print(CountPalindromicSubString("nitin"))
# subString("1234")