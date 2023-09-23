def maxArea(height: list[int]) -> int:
    l,r=0,0
    maxVol=0
    hieghtLen=len(height)
    for i in range(hieghtLen):
        print("==================", maxVol)
        for j in range(i, hieghtLen):
            print("i=", i, "h[i]=", height[i])
            print("j=", j, "h[j]=", height[j])
            vol=min(height[i], height[j]) * (j-i)
            maxVol=max(maxVol, vol)
            print("----------------len=", j-i, "vol=", vol, "maxV", maxVol)
            
    return maxVol

print(maxArea( [1,8,6,2,5,4,8,3,7]))