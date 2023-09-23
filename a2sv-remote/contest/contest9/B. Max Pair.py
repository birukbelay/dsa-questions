# https://codeforces.com/gym/429357/problem/B


b= int(input())
boys = [int(a) for a in input().split()]
boys.sort()

g= int(input())
girls = [int(a) for a in input().split()]
girls.sort()
ctr=0
bi,gi=0,0

while bi<b and gi<g:
    if abs(boys[bi]-girls[gi]) <=1:
        ctr+=1
        bi+=1
        gi+=1
    else:
        if boys[bi]>girls[gi]:
            gi+=1
        else:
            bi+=1
print(ctr)





