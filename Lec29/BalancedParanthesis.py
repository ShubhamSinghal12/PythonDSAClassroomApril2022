s = "({})[])"

def isbal(s):

    st = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            st.append(i)
        else:
            if len(st) == 0:
                return False
            elif i == ")" and st[-1] != "(":
                return False
            elif i == "}" and st[-1] != "{":
                return False
            elif i == "]" and st[-1] != "[":
                return False
            
            st.pop()

    return len(st) == 0


def isbal2(s):
    st = []
    for i in s:
        if i == "(":
            st.append(")")
        elif i == "[":
            st.append("]")
        elif i == "{":
            st.append("}")
        elif len(st) == 0 or i != st[-1]:
            return False
        else:
            st.pop()
    
    return len(st) == 0

print(isbal2(s))