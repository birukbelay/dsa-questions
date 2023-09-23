import sys
input = sys.stdin.readline
# from collections import Counter

a = [int(j) for j in input().strip()]
s = [int(j) for j in input().strip()]


s.sort(reverse=True)

num= min( len(s),len(a))
ctrA=0
ctrS =0


while ctrA<len(a) and ctrS < len(s):
    if s[ctrS]> a[ctrA]:
        a[ctrA] = s[ctrS]
        ctrA+=1
        ctrS+=1
    else:
        ctrA +=1
print(int(''.join(map(str, a))))





# ans=0

# for i in range(len(a)):
#     ans += a[i]
#     ans *=10
# print(ans//10)


