# y=[2, 5J, 6]
# # y.sort()
# # print(y)

# d=[1,2,3,4]
# def i(x):
#     return x+1
# # print(list(map(i,d)))

# b=[sum(d[0:x+1]) for x in range(0, len(d))]
# # print(b)
# import re
# res = re.findall('Welcome to Turing', 'Welcome', 1)
# # print(res)


# t='%(a)s %(b)s %(c)s'
# print(t % dict(a='welcome', b="to", c="Turing"))

# print("Welcome to TURING".capitalize())

# alph="abcd"
# for i in range(len(alph)):
#     alph[i].upper()
# # print(alph)

# inpu=["noe", "rex", "vue"]
# for i in inpu:
#     inpu.append(i.upper())
# print(inpu)

def add(c, k):
    c.test=c.test +1
    k=k+1
class Plus:
    def __init__(self):
        self.test =0
def main():
    p=Plus()
    index =0
    for i in range(0,25):
        add(p, index)

    print("p.te", p.test)
    print("ind", index)
# main()

l=[1,2,3,4,5]
m=map(lambda x: 2**x, l)
# print(list(m))

# x="abcdef"
# i="a"
# while i in x[:-1]:
#     print(i, end="")

# a=[1,2]
# b=[2,1]
# print(a==b)
# print(set(a)==set(b))


# data=[10,20,30,40,50]
# data.pop()
# print(data)
# data.pop(2)
# print(data)

# 'the{} side {1} {2}'.format("brig", "of", "life")

# open(file="")
print(2**(3**2), (2**3)**2, (2**3)**3)