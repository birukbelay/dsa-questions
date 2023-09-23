from collections import deque

# stack = deque()
 
# append() function to push
# element in the stack
# stack.append('a')
# print(stack.peek())

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    
    stack = []
    obj={}
    final_arr=[]
    
    for i in range(len(nums2)):
        while  len(stack)>0 and stack[-1]<nums2[i] :
            
            if not stack:
                stack.append(nums2[i])
                break
            val=stack.pop()
            obj[val]=nums2[i]
        stack.append(nums2[i]) 
        # print(obj) 
    for i in range(len(nums1)):
        # print(final_arr)
        # print("ii-",nums1[i],i)
        
        if nums1[i] in obj:
            a=obj[ nums1[i] ]
            final_arr.append( int( a ))
        else:
            final_arr.append(-1)
      
    return final_arr

            
print(nextGreaterElement( [4,1,2], [1,3,4,2]))           
print(nextGreaterElement( [2,4], [1,2,3,4] ))           