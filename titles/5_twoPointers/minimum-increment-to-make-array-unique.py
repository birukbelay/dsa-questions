class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        dicn={}
        print(nums)
        ctr=0
        lstCtr=0
        for i in nums:
            tempN=i
            
            # print("num=",i)
            if i not in dicn:
                # print("i not in dic--", i)
                dicn[i]=1
                continue
            else:
                # print("i in dicn--", tempN, lstCtr)
                if tempN<lstCtr:
                    ctr+=lstCtr-tempN
                    tempN=lstCtr
                    
                    
            while tempN in dicn:
                # print("tempN in", tempN)
                tempN+=1
                ctr+=1
                if tempN not in dicn:
                    dicn[tempN]=1
                    lstCtr=tempN
                    # print(dicn)
                    break
                # print("tempN -==--", tempN, ctr)
        return ctr
        