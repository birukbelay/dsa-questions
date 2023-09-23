#x https://codeforces.com/gym/429357/problem/A
import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())


for i in range(n):
    j= int(input())
    num= input().strip()
    # print('--', num)
    def give(num, j):
        l,r=0,j-1
        while l<=r:
            if num[l]!= num[r]:
                # print("-->",r,l)
                l+=1
                r-=1
            else:
                return (r-l)+1
        return 0
    print(give(num, j))

