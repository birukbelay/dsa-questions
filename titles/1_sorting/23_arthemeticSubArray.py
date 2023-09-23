def checkArithmeticSubarrays( nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    list=[]
    for i in range(len(l)):
        arr=nums[ l[i]:r[i]+1]
        arr.sort()
        sum1=arr[1]-arr[0]
        hold=True
        print("i=", i, "arr=", arr)  
        for j in range(len(arr)-1):                      
            if arr[j+1]- arr[j] !=sum1:
                list.append(False)
                hold=False
                break
        if hold:
            list.append(True)
    return list
# print(checkArithmeticSubarrays( [4,6,5,9,3,7], [0,0,2], [2,3,5] ))        
print(checkArithmeticSubarrays( [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7],  [4,4,9,7,9,10] ))        