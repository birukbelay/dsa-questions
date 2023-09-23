# https://leetcode.com/problems/basic-calculator-ii/

from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        symbols=["/", "*", "+", "-"]
        q = deque()
        q2= deque()
        
#         # create a stack of symbols and numbers
#         j=0        
#         while j <len(s):
            
#             if s[j] !=" ":                
#                 tempNum=""
#                 cnt=j                
# #     -------------     this is to find a multi digit number
#                 while cnt<len(s) and s[cnt] not in symbols:
                    
#                     tempNum+=s[cnt]
#                     cnt+=1
#                 if len(tempNum)>1:
#                     # print("-------", tempNum)
#                     q.append(tempNum)
#                     j+=cnt-j
#                 else:
#                     q.append(s[j])            
#             j+=1
#         print("stack=", q)  
        temp=""
        for i in s:
            if i in symbols:
                q.append(temp)
                temp=""
                q.append(i)                
            else:
                temp+=i
        q.append(temp)
        print("stack=", q)         
        while q:
            sym=q.popleft()
            if sym=="/":
                num2=q2.pop()
                num1=q.popleft()
                result=int(num2)//int(num1)
                q2.append(result)
            elif sym=="*":
                num1=q.popleft()
                num2=q2.pop()
                result=int(num2)*int(num1)
                q2.append(result)
            else:
                q2.append(sym)
        
        q2, q=q,q2        
        
        while q:
            sym=q.popleft()
            if sym=="+":
                num1=q.popleft()
                num2=q2.pop()
                result=int(num2)+int(num1)
                q2.append(result)
            elif sym=="-":
                num1=q.popleft()
                num2=q2.pop()
                result=int(num2)-int(num1)
                q2.append(result)                
            else:
                q2.append(sym)
        q2, q=q,q2       
        
        
        return int(q[0])
        
            
            
            
        