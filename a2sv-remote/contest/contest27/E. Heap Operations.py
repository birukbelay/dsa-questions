import sys

input = sys.stdin.readline
import heapq

t = int(input())
heap=[]
logs = []
for _ in range(t):
    uinput= input()
    arr = uinput.split()

    if arr[0]=="insert":
        heapq.heappush(heap, int(arr[1]))
        logs.append(uinput)
    elif arr[0]== 'removeMin':
        if len(heap) ==0:
            logs.append('insert 1')
            heapq.heappush(heap, 1)
        logs.append(uinput)
        heapq.heappop(heap)
    elif arr[0] == 'getMin':
        while heap and heap[0] < int(arr[1]):
            heapq.heappop(heap)
            logs.append("removeMin")
        if not heap or heap[0] > int(arr[1]):
            heapq.heappush(heap, int(arr[1]))
            logs.append('insert ' + arr[1])
        logs.append(uinput)
print(len(logs))
for i in logs:
    print(i)

