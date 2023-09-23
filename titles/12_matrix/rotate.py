def rotate(box):
    
    row= len(box)
    col= len(box[0])
    #a reversed matrix
    ans= [[0] * row for _ in range(col)]
    for i in range(row):
            for j in range(col):
                ans[j][row-1-i]= box[i][j]