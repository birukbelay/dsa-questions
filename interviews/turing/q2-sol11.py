
def soln(n, m, allGames):
    # this have lenght of n
    curGame=[]
    for game in allGames:
        d={}
        # make the player as key and his index as a value
        for playerIdx in range(len(game)):
            d[game[playerIdx]]=playerIdx
        #append the player game index into the dictionary
        curGame.append(d)

    # check the two players have been on opposite team 
    def check(p1, p2):
        played=False
        for i in curGame:
            N= len(i)
            if i[p1]<N/2 and i[p2] >=N/2:
                played=True
            elif i[p2]<N/2 and i[p1] >=N/2:
                played = True
        return played

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                continue
            played= check(i,j)
            if not played:
                return False
    return True

a=[
    [1 ,6, 3, 4 ,5, 2], 
    [6 ,4 ,2, 3, 1, 5] , 
    [4, 2, 1, 5, 6, 3], 
    [4, 5, 1, 6, 2, 3] ,
    [3, 2, 5, 1, 6, 4], 
    [2, 3, 6, 4, 1, 5]
    ]
b=[[3,1,4,5,6,2],
    [5,3, 2,4,1,6],
    [5,3,6,4,2,1],
    [6,5,3,2,1,4],
    [5,4,1,2,6,3],
    [4,1,6,2,5,3]

]
print(soln(1,0,[[1]]))