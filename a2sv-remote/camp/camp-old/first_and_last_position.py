

def findLeft(nums: list[int], target: int) -> int:    
    left=0
    right=len(nums)- 1
    best=0
    while left<= right:
        middle= (left+right)//2

        if nums[middle]==target:
            best= middle
            right=middle-1            
        elif nums[middle]> target:
            right = middle-1
        else:
            left=middle+1
        if best==left:
            return best
    return -1

def findRight(nums: list[int], target: int) -> int:    
    left=0
    right=len(nums)- 1
    best=0
    while left<= right:
        middle= (left+right)//2

        if nums[middle]==target:
            best= middle
            left=middle-1            
        elif nums[middle]> target:
            right = middle-1
        else:
            left=middle+1
        if best==right:
            return best
    return -1


def searchRange(self, nums: List[int], target: int) -> List[int]:
        left= findLeft(nums, target)