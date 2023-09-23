def merge(intervals):
    intervals.sort(key=lambda p: p[0])
    first= intervals[0][0]
    last = intervals[0][1]
    arr=[]   
    for i in range(len(intervals)):
        if intervals[i][0]<= last:
            if last < intervals[i][1]:
                last= intervals[i][1]
        else:
            arr.append([first,last])
            first=intervals[i][0]
            if last < intervals[i][1]:
                last= intervals[i][1]
            
        print("i", i)
        print("int", intervals)
        print("arr", arr)
        print("first", first)
        print("last", last)
        print("----")
    arr.append([first,last])
    return arr

print(merge( [[1,3],[2,6],[8,10],[15,18], [17,20]]))