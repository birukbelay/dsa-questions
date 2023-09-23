def cal(k):
    arr=[]
    while k>0:
        l=k%2                
        k//=2
        arr.append(l)
    l, r=0, len(arr)-1
    # reverse it
    while l<r:
        arr[l], arr[r]=arr[r], arr[l]
        l+=1
        r-=1
    return arr

print(cal(17))
print(cal(8))
print(cal(5))
print(cal(111))