
import heapq

def heapOpration():
    input1 = int(input(""))
    arr=[]
    ctr=0
    while ctr<input1:
        input2= input("")
        val=input2.split()
        
        if val[0]=="1":
            heapq.heappush(arr, int(val[1]))
        elif val[0]=="2":
            num=int(val[1])
            
            index = arr.index(num)
            num[index], num[-1]=num[-1], num[index]
            arr.pop()
            # heapq.heapify(arr)            
            heapq._siftup(arr, index)
            heapq._siftdown(arr, 0, index)
            
        elif val[0]=="3":
            print(arr[0])            
        ctr+=1
            

        
    
    