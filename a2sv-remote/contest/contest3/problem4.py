import sys
input = sys.stdin.readline


s = input().strip()

def correct(word):
    h="hello"
    l=0
    for i in range(len(word)):
        if word[i]==h[l]:
            l+=1
        if l>=len(h):
            return True
    return False

if correct(s):
    print("YES")
else:
    print("No")


