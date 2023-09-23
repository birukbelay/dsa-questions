# https://codeforces.com/gym/418150/problem/A
import collections


a= int(input())

for i in range(a):
    v= str(input())
    print(v)


# wish

s= str(input())

lists= s.split()

st = set(lists)

if len(st)>4:
    print("YES")
else:
    print("NO")

# --------------------- students

a= int(input())

for i in range(a):
    val= str(input())
    new = val.replace("#", " ")
    print(new, end="")

# ----------- good members

n= int(input())
a= str(input())
b = str(input)

stud = a.split()
bad= b.split()

sets = set(stud)

for i in bad:
    sets.discard(i)

ctr=0
for i in sets:
    # 
    d=collections.Counter(i)
    maxV = max(d.values())
    minV = min(d.values())
    if maxV==minV:
        ctr+=1
print(ctr)




# ----------------
import sys
input = sys.stdin.readline
import collections


n= int(input())
a= str(input())
b = str(input())

stud = a.split()
bads = list(b.split())
# print(bads)
sets = set(stud)
 
for i in bads:
    
    sets.discard(i)
# print(sets)
ctr=0
for i in sets:
    # makd a dictionary form the values
    d=collections.Counter(i)
    # print(d)
    maxV = max(d.values())
    minV = min(d.values())
    if maxV==minV:
        ctr+=1
print(ctr)



# -- traffic

n= int(input())

for i in range(n):
    a = str(input())
    b= str(input())

    j, s = a.split()
    firstG = None
    lastG=None
    dis=0
    for i,v in enumerate(b):
        if i=="g" and firstG==None:
            firstG = i
        if i=="g":
            lastG = i
    for i,v in enumerate(b):
        if v==s:
            if i<firstG:
                dis = max(dis,firstG -i)
            elif i< lastG:
                dis = max(lastG -i)
            else: 
                dis = max(dis, (j-i)+ firstG)
    print(dis)







