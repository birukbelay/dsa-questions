# https://codeforces.com/gym/428258/problem/D
import sys
input = sys.stdin.readline
from collections import Counter


# s = input().strip()
def findIdx(s):
    temp={}
    last=0
    uniCtr=0
    for i, v in enumerate(s):
        
        if v in temp:
            # print(i,v, uniCtr)
            if uniCtr> 26:
                break
            else:
                # print(i,v,  'd[v-',temp[v], "uql=",uniCtr, "lst=",last)
                last=max(last, temp[v]+1)
                temp[v]=i
                uniCtr= i-last
            
        else:
            if v!='?':
                temp[v]=i
        uniCtr+=1
        
    if uniCtr<26:
        # print(-1)
        return -1
    # print()
    return last
def nice(s):
    
    
    alphaD={}    
    for i in range(26):              
        alphaD[chr(i+65)]=0
    
    # TODO find index where it can fit a unique alphabet
    start= findIdx(s)
    
    if start==-1:
        return -1
    newS=s[start:start+26]
    print(start, newS)
    d = Counter(newS)
    if '?' in d:
        d.pop('?', None)
    
    missing=[]
    for k,v in alphaD.items():
        if k not in d:
            missing.append(k)
        else:
            if d[k]>1:
                
                return -1
    # create a new string
    l=0  
    ans=''      
    for j in range(len(s)):
        i=s[j]
        if i=='?':
            if j>=start and j< start+26:
                ans+=missing[l]
                l+=1
            else:
                ans+='X'
        else:
            ans+=i
    return ans
        
tests=[
    "ABC??FGHIJK???OPQR?TUVWXY?",    
    "WELCOMETOCODEFORCESROUNDTHREEHUNDREDANDSEVENTYTWO",
    
    "??????????????????????????",
    "AABCDEFGHIJKLMNOPQRSTUVW??M",
    "QWERTYUIOPASDFGHJKL???????",
    "ABABABBAB????????????ABABABABA???????????ABABABABA?????????KLCSJB?????????Z",
    "Q?E?T?U?O?A?D?G?J?L?X?V?MMQ?E?T?U?O?A?D?G?J?L?X?V?N"
]
# ans=[
#    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    -1,
#     "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
#     -1,
#     "QWERTYUIOPASDFGHJKLBCMNVXZ",
#     "ABABABBABXXXXXXXXXXXXABABABABAXXXXXXXXXXXABABABABADEFGHIMNOKLCSJBPQRTUVWXYZ"
#     "QXEXTXUXOXAXDXGXJXLXXXVXMMQBECTFUHOIAKDPGRJSLWXYVZN",


# ]
# for i in range(len(tests)):
#     print(nice(tests[i]))
ts='TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNRFYMKSZXHCLBQV?TUEJOIPWGNR'
print(nice(ts))
    
