class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        currProduct = 1
        minimum = 0
        subArrays = 0
        total = 0
        
        for i in range(len(nums)):
            # Calculate the product so fat and calculate sub arrays
            currProduct *= nums[i]
            subArrays += 1
            
            # While loop to increse the minimum and decrese the sun arrays
            while currProduct >= k and minimum <= i:
                currProduct /= nums[minimum]
                minimum += 1
                subArrays -= 1

            # add the sub Arrays to total if currProduct is less than k
            if currProduct < k:
                total += subArrays
        return total