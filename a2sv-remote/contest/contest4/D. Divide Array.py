# https://codeforces.com/gym/422879/problem/D 
import sys
input = sys.stdin.readline


n= int(input())
# arr= input().split()
iarr = [int(a) for a in input().split()]
# iarr.sort()

d={}
narr=[]
zarr=[]
parr=[]
for i in iarr:
    if i>0:
        parr.append(i)
        # d[1]=d.get(1, 0) +1
    elif i==0:
        zarr.append(i)
        # d[0]=d.get(0, 0) +1
    else:
        narr.append(i)
        # d[-1]=d.get(-1, 0) +1
p=len(parr)
ne=len(narr)
z=len(zarr)
if p>0:
    if ne%2==0:
        zarr.append(narr.pop())
else:
    if ne%2==0:
        parr.append(narr.pop())
        parr.append(narr.pop())
        zarr.append(narr.pop())
    else:
        parr.append(narr.pop())
        parr.append(narr.pop())
print(len(narr))
for i in narr:
    print(i, end=" ")
print()
print(len(parr))
for i in parr:
    print(i, end=" ")
print()
print(len(zarr))
for i in zarr:
    print(i, end=" ")







# pos=d[1]
# neg=d[-1]
# zer=d[0]
# if pos>0:
#     if neg%2==0:
#         #neg
#         print(neg-1)
#         print(arr[:neg-1])
#         #pos
#         print(pos)
#         print(arr[neg+zer:])
#         #zero
#         print(zer+1)
#         print(arr[neg-1:neg+zer])
        
#     else:
#         print(neg)
#         print(arr[:neg])
#         #pos
#         print(pos)
#         print(arr[neg+zer:])
#         #zero
#         print(zer)
#         print(arr[neg:neg+zer])
        
# else:
#     if d[-1]%2==0:
#         #bcs it will give 2 to the posetive
#         print(neg-3)        
#         print(arr[2:neg-1])
#         #pos
#         print(2)
#         print(arr[:2])
#         #zero
#         print(zer+1)
#         print(arr[neg-1:])
#     else:
#         print(neg-2)                
#         print(arr[2:neg])
#         #pos
#         print(2)
#         print(arr[:2])
#         #zero
#         print(zer)
#         print(arr[neg:])
    
