import sys
input = sys.stdin.readline
import collections
import re
from string import digits

# s = "12James potter"

n= int(input())

def getInt(s):
    new_result = re.findall('[0-9]+', s)
    return int(new_result[0])

def removeInt(s):
    remove_digits = str.maketrans('', '', digits)
    a= s.translate(remove_digits)
    return a.replace("\n", "")
    

for i in range(n):

    s = str(input())

    lst = s.split(" ")
    lst.sort(key=getInt)
    
    newLst = [ removeInt(x) for x in lst]
    newS= " ".join(newLst)
    # print(newLst)
    print(newS)
    # print(end="\n")
    