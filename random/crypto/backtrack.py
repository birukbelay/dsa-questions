
def back(str):
    arr = str.split(" ")
    tot=""
    for i in arr:
        val = reverse(i)
        tot+=val
    return tot
    
    
    
def reverse(str):
    i,j=0, len(str)-1
    lst=[0]* len(str)
    while i<=j:
        lst[i],lst[j] = str[j], str[i]
        j-=1
        i+=1
    return "".join(lst)
    
print(reverse("abcdef"))

print(back("abc def jkl"))