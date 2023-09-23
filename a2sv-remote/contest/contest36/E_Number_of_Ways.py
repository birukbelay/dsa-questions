# sliding window with prefix sum
import sys
input = sys.stdin.readline
import heapq
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]

# make a prefix fum
prefix = arr[:]
for i in range(1, len(arr)):
    prefix[i] += prefix[i-1]

suffix = arr[:]

for i in range(len(arr)-2, -1,-1):
    suffix[i] += suffix[i+1]

totSum = suffix[0]
print(suffix, prefix)
if totSum%3 !=0:
    print(0)
    exit()
target = totSum//3

tot =0
# for i in range(n):
#     if prefix[i] == target:
#         ctr+=1
#     if prefix[i] == target*2:
#         tot += ctr
# print(tot)

preHeap =[]
sufHeap =[]
for i in range(n):
    if prefix[i]==target:
        preHeap.append(prefix[i])
for i in range(n-1, -1, -1):
    if suffix[i]== target:
        heapq.heappush(sufHeap, suffix[i])        
# tot=0
print(preHeap)
print(sufHeap)
while sufHeap:
    cur = sufHeap[0]
    for i in prefix:
        while i+1>= cur:
            
            if sufHeap:
                
                heapq.heappop(sufHeap)
                if sufHeap:
                    cur= sufHeap[0]
            else:
                break
        if sufHeap:
            tot+= len(sufHeap)
print(tot)
# # for i in  preHeap:
#     for j in sufHeap:
#         if j> i+1:
#             tot+=1
#         else:
#             break


# 0, 2, 3

# 0, 1, 3




# [0, 1, -1, 0]
# [0, 1, 0, 0]
#  i     j  
# make a sliding window







# ways= 0
# for i in range(len(arr)-2):
#     for j in range(i+1, len(arr)-1):

#         firstPart = prefix[i]
#         middlePart = prefix[j]- prefix[i]
#         lastPart = prefix[len(arr)-1]- prefix[j]

#         if firstPart == middlePart == lastPart:
#             ways +=1
# print(ways)