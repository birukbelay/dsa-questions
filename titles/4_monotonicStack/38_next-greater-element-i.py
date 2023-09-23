def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack=[]
    dicn={}
    nxtElements=[]
    for i in range(len(nums2)):
        while stack and stack[-1]<nums2[i]:
            a=stack.pop()
            dicn[a]=nums2[i]
        stack.append(nums2[i])
        
    for i in nums1:
        if i in dicn:
            nxtElements.append(dicn[i])
        else:
            nxtElements.append(-1)
    return nxtElements    

         