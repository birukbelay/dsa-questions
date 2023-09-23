import sys
input = sys.stdin.readline



s1 = input().strip()
s2 = input().strip()

if s1.lower() < s2.lower():
    print("-1")
elif s2.lower() < s1.lower():
    print("1")
else:
    print("0")

