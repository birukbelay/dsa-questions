import sys
input = sys.stdin.readline


n= int(input())
l = input().split()

cl =[int(i) for i in l]
cl.sort(reverse=True)
tot= sum(cl)

his=tot
mine=0
for i in range(len(cl)):
    mine+=cl[i]
    his -=cl[i]
    if mine>his:
        print(i+1)
        break


