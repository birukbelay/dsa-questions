import sys
input = sys.stdin.readline
# from collections import Counter

n= int(input())
arr = [int(a) for a in input().split()]
s = input().strip()

for i in range(n):
    arr = [int(a) for a in input().split()]
    s = input().split()     # for string with spaces
    s=[a for a in input().strip()] # for strings with no spaces
    s = input().strip()

ord(a) #97
chr(97) #a

N = input()                             # returns a string
N = int(input())                        # returns a single integer
                                     
# if the input is given as some spaced integers
A = input().split()                     # returns an array of strings
A = [int(i) for i in input().split()]   # returns an array of integers
C,D = [int(i) for i in input().split()] # returns two integer variables C & D 
[ print(a, end=" ") for a in newArr]    # prints an array



# graph
n, m = [int(a) for a in input().split()]
d = defaultdict(list)
for i in range(m):
    a, b = [int(a) for a in input().split()]
    d[a].append(b)
    d[b].append(a)