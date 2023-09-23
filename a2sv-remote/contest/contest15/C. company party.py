# https://codeforces.com/gym/436386/problem/C
import sys
input = sys.stdin.readline

# this question is knowing the hight of a given tree
n=int(input())

tree={}
# arr=[-1,1,2,1,-1,3,5]
for i in range(n):
    # s=arr[i]
    s=int(input())
    vm=tree.get(s, [])
    vm.append(i+1)
    # print("vmmmm", vm)
    tree[s]= vm
    # print(tree)
    
class soln:
    
    def __init__(self):
        self.maxDepth=0
    def getSoln(self):
        self.findDepth(-1, 0)
        return self.maxDepth

    def findDepth(self, node, curDepth):
        # print(node, "dept",curDepth)
        if not node in tree:
            self.maxDepth=max(self.maxDepth, curDepth)
            return
        

        for cld in tree[node]:
            # print(cld)
            self.findDepth(cld, curDepth+1)
s=soln()    
print(s.getSoln())