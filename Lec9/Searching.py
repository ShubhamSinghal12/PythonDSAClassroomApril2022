ll = [[1,3,5,7],[2,6,6,9],[3,8,10,12],[4,10,11,15]]

def search(ll,ele):
    i = 0
    j = len(ll[0])-1

    while i < len(ll)-1 and j > 0:
        if ll[i][j] == ele:
            return True
        elif ll[i][j] > ele:
            j -= 1
        else:
            i += 1
    
    return False

print(search(ll,13))