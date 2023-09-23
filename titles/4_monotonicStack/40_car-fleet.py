def meetingDistance(p1,v1, p2, v2):
    
    if (v2>v1 and p2>p1) or (v2<v1 and p2<p1) or (v2==v1 and p2<p1) or (v2==v1 and p2>p1):
        print("c1=",p1,v1, "  c2==", p2,v2, "=---", -1)
        return -1        
    dis=(p1*v2 - p2*v1)/(v2-v1)
    print("c1=",p1,v1, "  c2==", p2,v2, "=---", dis)
    return dis
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        dicn={}
        fleetCtr=0
        # sorting the cars by their positions
        for i in range(len(position)):
            dicn[position[i]]=speed[i]
        sd = sorted(dicn.items())
        print("sd==",sd)
        print("-------------------------------------")
        prevFleetDis=0
        prevFleetSpeed=0
        loopCtr=0        
        while len(sd)>0:
            print(loopCtr,"|->",sd, "fltCtr=", fleetCtr)
            c2=sd.pop()
            c1=(0,0)            
            if len(sd)>0:
                c1=sd.pop()
            else:
                break                
                # return fleetCtr+1
            
            dis=meetingDistance(c1[0], c1[1],c2[0], c2[1])
            print("dis=", dis, "fleetCtr-", fleetCtr)
            # if the cars meet at some point
            if 0<=dis <=target:                
                # sd.append((dis, c2[1]))                                    
                prevFleetDis=dis
                prevFleetSpeed=c2[1]
                sd.append(c1)                
                print("|||joined the fleet2 at->",dis, sd)
                print("prevFleetV==", prevFleetDis, prevFleetSpeed)
            else:
                print("Cant Catch up car==", dis)     
                # if he cant catch the car, we check if he can catch the fleet
                dis2= meetingDistance(c1[0], c1[1], prevFleetDis, prevFleetSpeed)
                print("***dis2--", dis2) 
                if 0<=dis2 <= target:
                    print(">>just joined the fleet")
                    prevFleetDis=dis2                    
                else:
                    fleetCtr+=1     
                    print("-------------------------------new fleet Car```````",fleetCtr, "leader==", c1)                    
                sd.append(c1)
            loopCtr+=1
        
        return fleetCtr 
    
    

def test(rtrn, expectd):
    if rtrn==expectd:
        print("=======>True")
    else:
        print("========>False", "expected=", expectd, "got=", rtrn)
        
        
sol=Solution()
# test(sol.carFleet(13,[10,2,5,7,4,6,11], [7,5,10,5,9,4,1]), 2)
# test(sol.carFleet(100, [0,2,4],  [4,2,1]), 1)
# test(sol.carFleet(12, [10,8,0,5,3],  [2,4,1,1,3]), 3)



def car_fleet(destination, position, speed):
    car_speed_map={}
    for i  in range(len(position)):
        car_speed_map[position[i]]=speed[i]
    position.sort(reverse=True)
    fleet_count=0
    current_fleet_finish_time=(destination-position[0])/car_speed_map[position[0]]
    for i in range(1, len(position)):
        finish_time=(destination - position[i])/car_speed_map[position[0]]
        if finish_time>current_fleet_finish_time:
            fleet_count+=1
            current_fleet_finish_time=finish_time
    fleet_count+=1
    return fleet_count


def carFleet(target: int, position: list[int], speed: list[int]) -> int:        
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    target=float(target)
    times=[]
    print(len(position))
    for i in range(len(position)):
        times.append((target-position[i])/speed[i])
    print(times)
    PositionTimePair=[[pos,time] for pos,time in zip(position, times)]
    PositionTimePair.sort(reverse=True) 
    print(PositionTimePair)
    flt=[0] 
    for p,t in PositionTimePair:
        if flt[-1]<t:
            flt.append(t)    
    return len(flt)-1

# test(carFleet())
test(carFleet(13,[10,2,5,7,4,6,11], [7,5,10,5,9,4,1]), 2)
# test(carFleet(100, [0,2,4],  [4,2,1]), 1)
# test(carFleet(12, [10,8,0,5,3],  [2,4,1,1,3]), 3)