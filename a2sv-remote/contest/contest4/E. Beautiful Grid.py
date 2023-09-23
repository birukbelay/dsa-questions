# https://codeforces.com/gym/422879/problem/E
# Hint
# https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
# https://codeforces.com/gym/422879/problem/E
# Hint
# https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

import sys
input = sys.stdin.readline


n= int(input())
def updateMat(mat,v,i,j, val):
    mat[i][j] = val
    mat[j][v-1-i]= val
    mat[v-1-i][v-1-j]= val
    mat[v-1-j][i]= val

for i in range(n):
    v= int(input())
    mat=[]
    for i in range(v):
        r= input().strip()
        irow=[int(a) for a in r]
        mat.append(irow)
    ctr=0
    for i in range(v):
        for j in range(v):
            cur = mat[i][j]
            r90= mat[j][v-1-i]
            r180 = mat[v-1-i][v-1-j]
            r270 = mat[v-1-j][i]
            if cur==r90==r180==r270:
                continue
            elif sum([cur, r90, r180, r270]) ==2:
                updateMat(mat, v, i,j,0)
                ctr+=2
            else:
                ctr+=1
                if sum([cur, r90, r180, r270])==1:
                    updateMat(mat, v, i,j,0)
                else:
                    updateMat(mat, v, i,j,1)
    print(ctr)

    

            


    


