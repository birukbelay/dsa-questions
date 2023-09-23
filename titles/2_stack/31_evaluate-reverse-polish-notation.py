# https://leetcode.com/problems/evaluate-reverse-polish-notation/


    
    
import re


def evalRPN(tokens: list[str]) -> int:
        stack=[]
        symbols={"+":1, "-":1,"*":1,"/":1}
        
        def cal(val):
            v1, v2=stack.pop(), stack.pop()
            if val == "+": return v2+v1
            elif val=="-": return v2-v1
            elif val=="*": return v2 *v1
            elif val=="/": return int(v2/v1)
        
        for i in tokens:
            print(stack)
            if i in symbols:
                stack.append(cal(i))
        #     if i == "+":
        #         first=stack.pop()
        #         second=stack.pop()
        #         stack.append(first+second)
        #     elif i=="-":
        #         first=stack.pop()
        #         second=stack.pop()
        #         stack.append(second-first)
        #     elif i=="*":
        #         first=stack.pop()
        #         second=stack.pop()
        #         stack.append(second*first)
        #     elif i=="/":
        #         first=stack.pop()
        #         second=stack.pop()
        #         if abs(second)<abs(first):
        #             stack.append(0)
        #         else:
        #             stack.append(int(second/first)) 
            else:
                stack.append(int(i))
        return stack[0]
    
    
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(6//-132)
# print(-4//123)
lst=["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]

print(evalRPN(lst))