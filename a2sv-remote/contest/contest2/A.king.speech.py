import sys
input = sys.stdin.readline
import collections

n= int(input())

def stutter(word):
    w= word.replace("\n", "")
    return print(f'{word[:2]}... {w}?')
    
for i in range(n):
    a = str(input())
    stutter(a)