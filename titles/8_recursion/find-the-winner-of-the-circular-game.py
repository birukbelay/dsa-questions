# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ctr=0
        
        lst=[]
        for i in range(n):
            lst.append(i+1)
        return self.winner(lst, k,0)
    def winner(self, arr, k, i):
        if len(arr)==1:
            return arr[0]
        else:
            idx=self.findCircle(arr, k, i)
            # print("delting the idx==-----", idx,"arr[idx]=", arr[idx])
            del arr[idx]
            return self.winner(arr, k, idx)
            
    def findCircle(self,arr, k, i):
        ctr=0
        idx=i
        # print("arr=",arr, "i=",i)
        while ctr<k:
            if idx==len(arr)-1:
                idx=0
                ctr+=1
            elif idx>len(arr)-1:
                idx=1
                ctr+=1
            else:
                idx+=1
                ctr+=1
        # print("idx=",idx-1,)
        # print( arr[idx-1])
        if idx==0:
            # print("zarr=", arr, len(arr))
            return len(arr)-1
        return idx-1