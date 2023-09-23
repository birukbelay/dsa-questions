# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

# You are given an array of strings nums and an integer k.
# Each string in nums represents an integer without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. 
# For example, if nums is ["1","2","2"], "2" is the first largest integer,
# "2" is the second-largest integer, and "1" is the third-largest integer.

def kthLargestNumber( nums: list[str], k: int) -> str:
        nums.sort(key=lambda p: int(p))
        print(len(nums)-k)
        a=len(nums)-k
        print(nums)
        return nums[a]
print(kthLargestNumber(["3","6","7","10"], 4))   