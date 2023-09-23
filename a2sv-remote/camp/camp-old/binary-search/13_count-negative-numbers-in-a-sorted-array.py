# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        sum=0
        for i in grid:
            left=0
            right=len(i)
            if i[0]<0:
                sum+=len(i)
                continue
            elif i[-1]>=0:
                continue
            while left<right:
                middle=(left+right)//2
                if i[middle]<0:
                    right=middle-1
                    if i[middle-1]>=0:
                        sum+= len(i)-middle
                        break
                else:
                    left= middle+1
                    if i[middle+1]<0:                        
                        sum+=len(i)-middle-1                        
                        break
        return sum