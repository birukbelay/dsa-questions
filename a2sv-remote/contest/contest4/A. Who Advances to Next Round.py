import sys
input = sys.stdin.readline

s = input().split()
k= int(s[1])-1
lst = input().split()


def output():
    if lst[0]== "0":        
        return 0    
    val = int(lst[k])
    j=k
    if val==0:
        # print("here")
        while j>=0 and lst[j]=="0":

            j-=1
        return j+1
    ctr=k
    l=k+1
    while l< len(lst) and int(lst[l]) == val:
        # print("here")
        ctr+=1
        l+=1
    return ctr +1
print(output())