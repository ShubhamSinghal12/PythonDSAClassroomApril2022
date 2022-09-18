def wine(casks,si,ei):
    y = len(casks) - (ei-si)
    if si == ei:
        return casks[si]*y
    else:
        f = casks[si]*y+wine(casks,si+1,ei)
        s = casks[ei]*y+wine(casks,si,ei-1)
        return max(f,s)
