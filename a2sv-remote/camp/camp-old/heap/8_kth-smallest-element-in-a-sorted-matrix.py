import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heapArr=[]
        ctr=0
        for i in matrix:
            for j in i:
                if ctr>=k:                                            
                    heapq.heappush(heapArr, -j) 
                    heapq.heappop(heapArr)
                else:
                    heapq.heappush(heapArr,-j)
                ctr+=1
                    

        print(-heapArr[0]) 
        return -heapArr[0]
    
soln=Solution()
soln.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)