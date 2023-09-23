def lastNonLeaf(a):
    return len(a)-2//2 
def LChildIndex( index):
        return 2*index +1  
def RChildIndex(index):
        return 2*index +2
def checkMinHeap(a):
     
    for i in range(lastNonLeaf(a)+1):
        leftInValid=  a[i] > a[LChildIndex(i)]
        
        # check if right child is not last child //true allways, exept last
        rIsNotLast=RChildIndex(i) != len(a)
        
        rightInValid= rIsNotLast and  a[i]>a[RChildIndex(i)]
        
        
        # r=(2*i + 2 != len(a) and a[i] > a[2*i + 2])
        
        
        # if a[i] > a[LChildIndex(i)] or (RChildIndex(i) !=len(a) and a[i]>a[RChildIndex(i)] )
        if leftInValid or rightInValid:
            return False
        
    return True