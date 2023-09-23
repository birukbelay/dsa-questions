def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs=[]
        total =0
        for i,ele in enumerate(nums):
            for j, ele2 in enumerate(nums):
                if (ele==ele2 and j>i):
                    pairs.append([i,j])
                    total+=1
        print(total, pairs) 
        return total