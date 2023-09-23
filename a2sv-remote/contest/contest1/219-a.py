
def make(k, s):
    d={}
    
    for i in s:
        d[i] = d.get(i, 0)+1
    st=""
    # print(d)
    # go len of s times
    for y in range(len(s)):
        # print("1-",i)
        
        #iterate over the dict values
        for i,v in d.items():
            if v%k !=0:
                return -1
            # print("bf---------", i,v)
            #iterate k times & add once to the string/ so we get ethe first one
            for j in range(k):                
                if v>=-1:                    
                    d[i] -= 1
            # print("st==",st)
            if v>0: st+=i
            # print("af", i,d[i])
    return st *k

import sys
# input = sys.stdin.readline
a= int(input())
k = str(input())          
print(make(2, "azza"))