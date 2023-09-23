def maxCoins( piles: list[int]) -> int:
    piles.sort()
    ind=len(piles)-2
    tot=0
    for i in range(len(piles)//3):
        tot+=piles[ind]
        ind-=2
    return tot   

print(maxCoins([9,8,7,6,5,1,2,3,4]))      
# print(maxCoins( [2,4,5]))      
    