import sys
input = sys.stdin.readline
# from collections import Counter
n=input().strip()
n1= int(n, 2)
n2= int(input(),2)

k=  n1^n2
j=len(n)
# print(j, n1)
# print(int(str(n^n2), 2))
print(f'{k:0{j}b}')
