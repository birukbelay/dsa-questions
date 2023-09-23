# https://codeforces.com/gym/425122/problem/C




import sys
input = sys.stdin.readline


def find():
    n= int(input())


    arr=[]
    for i in range(n):    
        s = input().split()
        arr.append((int(s[0]), int(s[1])))

    maxR= arr[0][1]
    minL= arr[0][0]

    for i in arr:
        maxR= max(maxR, i[1])
        minL= min(minL, i[0])
    for i, v in enumerate(arr):
        if v==(minL, maxR):
            return i+1
    return -1
print(find())














# # -----------------------------------
# import sys
# input = sys.stdin.readline

# n= int(input())
# invalidL=sys.maxsize
# invalidR=0
# maxDis=0
# idx=0

# maxR=0
# minL=sys.maxsize
# arr=[]
# for i in range(n):
    
#     s = input().split()
#     arr.append(int(s[0]), int(s[1]))

#     li=int(s[0])
#     ri=int(s[1])
#     # checking if this is bigger than the others
#     if ri-li> maxDis:
        
#         maxDis=ri-li  
#         # print(maxDis, ri, li)
#         if li<=minL and ri>=maxR:
#             # print("--",li, ri)
#             maxR= ri
#             minL= li
#             idx= i+1
#         else:    
#             if li< minL:
#                 invalidL = li
#             elif ri > maxR:
#                 invalidR = ri
#             maxR= ri
#             minL= li
#     else:
#         if li< minL:
#             invalidL = li
#         elif ri > maxR:
#             invalidR = ri
# # print("mx",maxR, minL)
# # print("in",invalidR, invalidL)
# if maxR>= invalidR and minL <= invalidL:
#     print(idx)
# else:
#     print(-1)