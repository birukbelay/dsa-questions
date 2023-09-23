import sys
input = sys.stdin.readline
import collections
 
n= int(input())
s= str(input())
 
lst= s.split(" ")
 
def output(n, lst):
    if n ==1:
        return 0
    symb= 0
    incCnt =0
    decCnt=0
    for i in range(1,n):
        #check dec
        if int(lst[i]) < int(lst[i-1]):
            if symb==0  or symb==1:
                symb=-1
                decCnt+=1
        #check inc
        if int(lst[i]) > int(lst[i-1]):
            if symb ==0 or symb ==-1:
                symb=1
                incCnt+=1
    return max(incCnt, decCnt)
print(output(n, lst))

def output2(n, lst):
    if n ==1:
        return 0
    maxN= lst[0]
    minN = lst[0]
    ctr=0
    for i in lst:
        if i > maxN:
            maxN=i
            ctr+=1
        if i<minN:
            minN=i
            ctr+=1
    return minN + maxN


