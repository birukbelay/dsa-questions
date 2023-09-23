def toDecimal(binArr):
    l=len(binArr)-1
    sum=0
    ctr=0
    for i in range(l,-1, -1):
        if binArr[i]==1:
            sum+= 2**ctr
        ctr+=1
    return sum
    
print(toDecimal([1,1,1]))