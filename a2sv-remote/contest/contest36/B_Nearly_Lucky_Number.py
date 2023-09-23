import sys
input = sys.stdin.readline
from collections import Counter

n= input().strip()

ctr= Counter(n)
numSum=ctr.get('4',0) + ctr.get('7',0) 
if numSum== 4 or numSum==7:
    print('YES')
else:
    print('NO')
