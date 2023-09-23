class Solution:
    def sumSubarrayMins(self, nums):
        MOD = 10**9+7
        stack = []
        res =  0
		prevsum = 0
		
        for index, value in enumerate(nums):
            count = 1
            while stack and stack[-1][0]>=value:
                v, c = stack.pop()
                count+=c
                prevsum-=v*c
            stack.append((value,count))
            prevsum+=value*count
            res+=prevsum
            
        return res%MOD


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        dl={}
        dr={}
        for i,v in enumerate(arr):
            # if the last element of the stack is greater than the array
            while stack and stack[-1][1]>v:
                idx,val=stack.pop()
                #right boundary for idx is current i
                dr[idx]=i
            
            dl[i]=stack[-1][0] if stack else -1            
            stack.append([i,v])
        while stack:
            i,v=stack.pop()
            dr[i]=-1
        ans=[1]*len(arr)
        tot=0
        for i in range(len(arr)):
            l=1
            if dl[i]==-1 and dr[i]==-1:
                # print("here")
                l=len(arr)#fixme                
            elif dl[i]==-1:
                l=dr[i]
                # print("l",l)                
            elif dr[i]==-1:                
                l=len(arr)-dl[i]-1
                # print('r',l)
            else:
                l=dr[i]-dl[i]
            print("=-",i,l)
            res= ((l**2)+l)//2
            
            tot+=res*arr[i]
            print(">>",tot,res)
            
        return tot
        
                
            
        