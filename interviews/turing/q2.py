
from collections import defaultdict

def sol(n, m, games):
    d={}
    #iterate over the games
    for matches in games:        
        N= len(matches)
        
        team1 = set(matches[:N//2])
        team2 = set(matches[N//2:]) 
        # iterate over each player for the matches       
        for p in matches:
            if p in team1:
                if p in d:
                    prev=d[p]
                    prev.update(team2)                    
                    d[p] = prev
                else:                    
                    d[p]= team2.copy()                    
            if p in team2:
                if p in d:                                        
                    prev=d[p]                    
                    prev.update(team1)                    
                    d[p] = prev                    
                else:                    
                    d[p]= team1.copy()
                    
    print(d)
    for i in range(1, n+1):
        matches=d[i]
        if len(matches)!= n-1:
            return False
    return True


def sol2(n, m, games):
    record=defaultdict(set)
    #iterate over the games
    for matches in games:        
        N= len(matches)
        
        team1 = set(matches[:N//2])
        team2 = set(matches[N//2:]) 
        # iterate over each player for the matches       
        for player in matches:
            if player in team1:
                record[player].update(team2)               
            else:
                record[player].update(team1)  
                    
    # print(record)
    for i in range(1, n+1):
        matches=record[i]
        if len(matches)!= n-1:
            return False
    return True

def sol3(n, m, games):
    record=defaultdict(set)
    #iterate over the games
    for matches in games:        
        N= len(matches)
        
           
        for index, player in enumerate(matches):
            if index< N//2:
                record[player].update(matches[:N//2])               
            if index >=N//2:
                record[player].update(matches[N//2:])  
                    
    # print(record)
    for i in range(1, n+1):
        matches=record[i]
        if len(matches)!= n-1:
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
print(sol2(6,6,a)==True)
print(sol2(6,6,b)==False)



# for i in a:
#     print(i)
#     N= len(i)

#     team1 = set(i[:N//2])
#     team2 = set(i[N//2:])
#     print("d=====================", d)
#     print("----> t1", team1)
#     print("--->t2", team2)
#     for p in i:

#         if p in team1:
#             if p in d:
#                 print("p=",p, d[p])
#                 print(type(d[p]))
#                 prev=d[p]
#                 # print("``````````team-", team2)
#                 # print("`````````prev",prev)
#                 prev.update(team2)
                
#                 print(">>>>>>>>>>prev=", prev)
#                 d[p] = prev
#                 print(">>>>>>>>>>d[p]=", d[p])
#             else:
#                 d[p]= team2
#         if p in team2:
#             if p in d:
#                 prev=d[p]
#                 prev.update(team2)
#                 d[p] = prev
#             else:
#                 d[p]= team1