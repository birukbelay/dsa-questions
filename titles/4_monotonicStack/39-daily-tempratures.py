class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        dicn={}
        nextList=[]
        for i in range(len(temperatures)):            
            while stack and stack[-1][0]< temperatures[i]:
                a=stack.pop()
                dicn[a[1]]=i-a[1]
            stack.append((temperatures[i],i))
        for i in range(len(temperatures)):
            if i in dicn:
                nextList.append(dicn[i])
            else:
                nextList.append(0)
                
        return nextList