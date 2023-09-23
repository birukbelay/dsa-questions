# https://leetcode.com/problems/accounts-merge/
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.root={}
        self.size= defaultdict(int)
        self.names={}
        
        
      
        # union to merge all accounts
        for i in range(len(accounts)):
            arr = accounts[i]
            
            for j in range(1,len(arr)):
                # save the name for each email adress
                self.names[arr[j]]= arr[0]
                self.union(arr[j], arr[-1])
            # to make sure the correct relation is not missed go over it again
            for j in range(1,len(arr)):                
                self.union(arr[j], arr[-1])
        # print("root--",self.root)
        
        
        cldList = defaultdict(set)
        
        for key, val in self.root.items():
            par = self.find(key)
            cldList[par].add(key)
        # print(ansD)
        ansArr =[]
        for key, val in cldList.items():
            usersEmails =[]
            # first add the name to the lists
            usersEmails.append(self.names[key])
            # add the rest of the emails to the users email arra
            name = sorted(list(val))
            for itms in name:
                usersEmails.append(itms)
            ansArr.append(usersEmails)
        return ansArr
            

    def find(self, node):
        if node not in self.root:
            self.root[node] = node
            return node
        if node ==self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self, x, y):        

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]