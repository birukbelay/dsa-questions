# https://leetcode.com/problems/kth-largest-element-in-a-stream/


import heapq
class KthLargest:
    nums=[]
    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)
        for i in range(len(nums)-k):
            heapq.heappop(self.nums)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        if len(self.nums)>0:
            print(self.nums[0])
            return self.nums[0]
        
kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3);   #// return 4
kthLargest.add(5);   #// return 5
kthLargest.add(10);  #// return 5
kthLargest.add(9);   #// return 8
kthLargest.add(4);  # // return