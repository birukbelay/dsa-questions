def countingDigits(n, cnt=0):    
    val=n//10
    count=cnt+1
    
    if val == 0:
        print( count)
        return count
    countingDigits(val, count)
        
    
def counting(n):
    count=0
    while n>0:
        n=n//10 
        count=count+1 
    print(count)
    
    return count   
    
# countingDigits(36666)
counting2(36666)


