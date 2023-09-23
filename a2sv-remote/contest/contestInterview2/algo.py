# childArr= graph
# ancestorCnt = incoming
order=[]
# 1. create a childrenArray and ancestorCount array
childArr = [[] for _ in range(num)]

ancestorCnt = [0 ] * num

# 2. append children & count ancesstor
for child, parent in keyPairs:
    childArr[parent].append(child)
    # count the parents each child has
    ancestorCnt[child] +=1
# 3. if person has no ancesror add to que
for ppl in range(num):
    if ancestorCnt[ppl]==0:
        que.append(ppl) 
#4. remove items from & decrease ancestorCnt of its children
while que:
    person= que.popleft()
    order.append(person)

    for child in childArr[person]:
        # this child has one less ancestor// this person
        ancestorCnt[child] -=1
        # 5. if item no more has ancestors left add it to que
        if ancestorCnt[child]==0:
            que.append(child)

