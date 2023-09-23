def isBadVersion(n):
    return n>=4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            middle=left+ (right-left)//2
            
            if isBadVersion(middle):
                print(f"badm={middle}")                
                right=middle-1
                if not isBadVersion(middle-1):
                    return middle
            else:
                left=middle+1
                print(f"Not-badm={middle}")  
                if isBadVersion(middle+1):
                    return middle+1
sol=Solution()
print(sol.firstBadVersion(5))