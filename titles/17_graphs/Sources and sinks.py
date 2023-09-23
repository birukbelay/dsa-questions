import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
# mat=[]
sink=defaultdict(list)
source=defaultdict(list)
for i in range(n):
    
    arr= input().split()
    for j in range(len(arr)):
        k=int(arr[j])
        if k==1:
            sink[i+1].append(j+1)
            source[j+1].append(i+1)
        else:
            sink[i+1]=sink.get(i+1,[])
            source[i+1]=source.get(i+1,[])

sinkArr=[]
sourceArr=[]
for key, value in sink.items():
    if len(value) ==0:
        sinkArr.append(key)
for key, value in source.items():
    if len(value) ==0:
        sourceArr.append(key)

print(len(sourceArr),*sourceArr)
print(len(sinkArr),*sinkArr)