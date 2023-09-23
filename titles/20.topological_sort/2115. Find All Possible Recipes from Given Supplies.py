class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        ans = []
        dep = defaultdict(list)
        ctr = defaultdict(int)
        suplySet= set()
        suplySet.update(supplies)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                # if the dependency is not in the supplys add it
                if ing not in suplySet:
                    dep[ing].append(recipes[i])
                    ctr[recipes[i]] +=1
        # print(dep)
        # print("ctr", ctr)
        que = deque()
        for itm in recipes:
            if ctr[itm] == 0:
                que.append(itm)
        print(que)
        while que:
            ingr = que.popleft()
            ans.append(ingr)

            for item in dep[ingr]:
                ctr[item] -= 1

                if ctr[item] == 0:
                    que.append(item)
        return ans
            







        