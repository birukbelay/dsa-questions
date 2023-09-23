def calculate(l):
    return (l[0]**2) + (l[1]**2)

def kClosest( points, k):
    l= len(points)
    pts_sorted=[]
    num_arr=[]
    for i in range(l):
        
        val = calculate(points[i])
        print("-")
        print("val1->",val)
        # num_arr.append(val)
        
        ctr=0
        while  ctr< len(num_arr) and num_arr[ctr]<val:
            ctr = ctr+1 
            print("l18,-num_arr", num_arr, "--ctr",ctr )
        
        print("l20ctr-", ctr)
        pts_sorted.insert(ctr, points[i])
        num_arr.insert(ctr, val)
                
        print("l24, numArr->", num_arr)
        print("l25, sortedPts-> ",pts_sorted)
        
    print(pts_sorted)
    return pts_sorted[:k]

print(kClosest([[3,3],[5,-1],[-2,4]], 2))

def kClosest2( points, k):
    print("==>",points)
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    print(points)
    return points[:k]

print(kClosest2([[3,3],[5,-1],[-2,4]], 2))



        