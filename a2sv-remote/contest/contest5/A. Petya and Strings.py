import sys
input = sys.stdin.readline


s1= input().strip()
s2= input().strip()

def compare(s1, s2):
    for i in range(len(s1)):
        n1= s1[i].lower()
        n2= s2[i].lower()


        if n1<n2:
            print(-1)
            return
        if n2< n1:
            print(1)
            return
    print(0)
compare(s1, s2)
    
