def targetIndices(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            if nums[i]==target:
                arr.append(i)
        return arr