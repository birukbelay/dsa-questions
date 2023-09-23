# https://www.hackerrank.com/contests/a2sv3-contest-6/challenges/qheap1
import heapq

def checkRoot(dicn, arr):     
    for key, value in dicn.items():
        if len(arr)==0:
            return
        if  value>0 and key==arr[0]:
            heapq.heappop(arr)
            dicn[key]=dicn[key]-1
   
def heapOpration():
    input1 = int(input())
    arr=[]
    ctr=0
    dicn={}
    while ctr<input1:
        input2= input()
        val=input2.split()
        
        if val[0]=="1":
            checkRoot(dicn, arr)
            heapq.heappush(arr, int(val[1]))            
        elif val[0]=="2":
            
            num=int(val[1])                      
            if num in dicn:
                dicn[num]=dicn[num]+1
            else:
                dicn[num]=1
            checkRoot(dicn, arr)
        elif val[0]=="3":
            checkRoot(dicn, arr)
            print(arr[0])            
        ctr+=1


class heapqs:
    dicn={}
    arr=[]
    def __init__(self):
        self.dicn={}
        self.arr=[]
    def insert(self,val):
        self.checkRoot(self.dicn, self.arr)
        heapq.heappush(self.arr, val) 
        print("insert-",self.arr)
    def remove(self, val):
        print("rmv arr=",self.arr)
        if val in self.dicn:
            self.dicn[val]=self.dicn[val]+1
        else:
            self.dicn[val]=1
        self.checkRoot(self.dicn, self.arr)
    def prnt(self):
        self.checkRoot(self.dicn, self.arr)
        print(self.arr[0])
        
    def checkRoot(self, dicn, arr):
        for key, value in dicn.items():        
            if key==arr[0] and  value>0:
                a=heapq.heappop(arr)
                dicn[key]=dicn[key]-1   
                print(a)
                print("arr@check",arr)
        
h=heapqs()

h.insert(4)
h.insert(9)
h.prnt()
h.remove(4)
h.prnt()
        
        