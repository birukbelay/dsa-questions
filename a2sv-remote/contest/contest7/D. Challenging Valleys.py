import sys
input = sys.stdin.readline


n= int(input())

def soln(arr):
    # print(arr)
    N=len(arr)
    j,i=0,0
    dis=0
    if N ==1:
        return True
    valleyCtr=0
    while i<N:
        if arr[i]== arr[j]:
            if j==0 or arr[j-1] > arr[j]:
                if i==N-1 or arr[i]<arr[i+1]:
                    valleyCtr+=1  
                
            i+=1
        else:
            j+=1
        # while arr[i]!=arr[j]:
        #     # print(i,j)
        #     j+=1
        # #from the left
        # if j==0 and i<N-1 and arr[j] ==arr[i]:
        #     if arr[i+1]> arr[i]:
        #         valleyCtr+=1
                
        # # rule one case
        # if j>0 and i<len(arr)-1 and arr[i]==arr[j]:
            
        #     if arr[j-1]> arr[j] and arr[i+1]> arr[i]:
        #         print("--")
        #         valleyCtr+=1
        
        # i+=1
        
    return True if valleyCtr==1 else False
for i in range(n):
    j=input()
    arr = [int(a) for a in input().split()]
    
    if soln(arr):
        print("YES")
    else:
        print("NO")



        

    