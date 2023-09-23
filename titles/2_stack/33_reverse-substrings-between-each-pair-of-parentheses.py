# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

def reverseString(s):
    newS=""
    print("s=",s)    
    for i in range(len(s),0,-1):
        # print(i,s[i-1])
        newS=newS+s[i-1]
    return newS
# print(reverseString("abebe"))  
def makeItAList(input):
    listOfStr=[]
    string=""
    # making a list of each componetn: "(u(love)i)"-->  ["(", "u","(", "love",")","i" ]
    for i in input:
        if i==")":
            listOfStr.append(string)           
            listOfStr.append(i)
            string=""            
        elif i=="(":
            if string!="":
                listOfStr.append(string)
            listOfStr.append(i)
            string=""
        else:
            string+=i
    if string!="":
        listOfStr.append(string)
    return listOfStr
# print(makeItAList("a(bcdefghijkl(mno)p)q"))         
# print(makeItAList("(u(love)i)"))         
def reverseParentheses(s: str) -> str:
    stack=[]
    listOfStr=makeItAList(s)
    
    print(listOfStr)
    for i in listOfStr:
        if i==")":
            a=stack.pop()
            # b=reverseString(a)
            # stack.pop()
            # stack.append(b)
            s=""
            while a !="(":
                s=a+s
                a=stack.pop()
            stack.append(reverseString(s)) 
            print("stac=>",stack)         
                                 
        else:
            stack.append(i)
    print(stack)
    return "".join(stack)
print(reverseParentheses("(u(love)i)") )
print(reverseParentheses("(ed(et(oc))el)") )
# print(reverseParentheses("a(bcdefghijkl(mno)p)q") )