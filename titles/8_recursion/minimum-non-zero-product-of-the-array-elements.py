# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/submissions/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # maxN=(2**p)-1
        
        MOD=10**9 +7 #->1000000007
#         top is the maximum number -> 7 ie,,111 //1111
        maxN = pow(2,p, MOD) -1
#     mid is the number right befor the maximum -> 6 ie 1110
        maxPair= maxN -1 
        
        # the mid count is half of the amount of numbers ie for 15 ==7, 7==3
        # this could just be maxNum-2/2    
        midcount=pow(2, p-1)-1 # 2**2 -1 == 1
        print(midcount)
        # midcount=maxN//2 #this dont work bcs maxN will be at max %MOD
        print(midcount)
        return (pow(maxPair, midcount, MOD)*maxN) %MOD
    
def makeDec(n):
    dec=""
    while n!=0:
        r=n%2
        n= //2
        dec=r+dec
    return int(dec)

def swap(a,b,n):
    lstA=list(a)
    lstB=list(b)    
    lstA[n],lstB[n]=lstB[n], lstA[n]
    a="".join(lstA)
    b="".join(lstB)
    return a,b
 
   
a="abebe"
b="bebede"
l=list(a)
ls=list(b)
l[0],ls[0]=ls[0],l[0]
print(l) 
print("".join(ls))   
t="01">"001"
print(t)