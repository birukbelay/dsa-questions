# https://codeforces.com/gym/420178/problem/E
import sys
input = sys.stdin.readline


s = input().split()
time = int(s[1])
lec = input().split()
sleep = input().split()
def theorem(time, lec, sleep):
    tot=0
    # calculating theorem count
    for i in range(len(lec)):
        if sleep[i]=="1":
            tot+= int(lec[i])

    maxTot=tot
    temp=tot
    l=0
    for i in range(len(lec)):
        if sleep[i]=='0':
            temp += int(lec[i])
        if i>=time:
            if sleep[l]=='0':
                temp-= int(lec[l])
            l+=1
        maxTot= max(maxTot, temp)
    return maxTot






    

