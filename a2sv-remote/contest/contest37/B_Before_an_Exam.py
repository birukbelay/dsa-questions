import sys
input = sys.stdin.readline
# from collections import Counter

days, sumTime = [int(a) for a in input().split()]
arr= []
minTime =0
maxTime =0
for _ in range(days):
    mi, ma = [int(a) for a in input().split()]
    arr.append((mi, ma))
    minTime +=mi
    maxTime +=ma


    
if sumTime> maxTime or sumTime< minTime:
    print("NO")
    
    exit()
# give each day the minimum hours it needs
ansArr=[val[0] for val in arr]
sumTime -= minTime

  

# iterate and give each day the max it needs until sumTime is 0

for i in range(days):
    diff = arr[i][1]- arr[i][0]
    if diff < sumTime:
        sumTime-=diff
        ansArr[i]+=diff
    else:
        ansArr[i]+=sumTime
        break
print("YES")
print(*ansArr)
