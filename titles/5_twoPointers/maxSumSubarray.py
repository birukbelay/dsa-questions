import imp


import sys
def maxSumSubarray(arr, k):
    maxVal=0
    sum=0
    
    for i in range(len(arr)):
        sum+=arr[i]
        if i>=k-1:
            maxVal=max(maxVal, sum)
            sum-= arr[i-(k-1)]
    print(max)
    return max