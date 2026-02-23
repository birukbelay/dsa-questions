from collections import defaultdict


def sol2(n, m, k):
    record = defaultdict(set)
	for match in k:
        N= len(match)
		#iterate over the match to update the players played set
		for index, player in enumerate(match):
            if index < N//2:
				record[player].update(match[:N//2])
			if index >= N//2:
				record[player].update(match[N//2:])
	# for each player from 1 upto n, check if he has played with all the players
	for i in range(1, n+1):
		if len(record[i])!=n-1:
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