# https://leetcode.com/problems/valid-parentheses/



def isValid( s: str) -> bool:
    stack = []
    # open=["{", "[", "("]
    dicn={"{":1, "[":1, "(":1}
    for i in range(len(s)):
        print("i=", i, "s[i]=", s[i])
        
        if s[i] in dicn:
            stack.append(s[i])            
        else:
            try:                
                a=stack.pop()
                if s[i]=="}" and a =="{":
                    continue
                elif s[i] =="]" and a =="[":
                    continue
                elif s[i] ==")" and a =="(":
                    continue
                
                else:
                    print("i=", i, "s[i]=", s[i], "a=", a)
                    return False
            except:
                return False
                

    if len(stack)==0:
        return True
    else:
        return False


# print(isValid("()"))
print(isValid("(]"))
# print(isValid("()[]{}"))