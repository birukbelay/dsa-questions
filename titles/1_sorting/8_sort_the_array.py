# l="hossa"
# print(l[-1])
# lists="hello my friens"

# print(lists.split())

def sort_array(s)-> str:
    
    arr= s.split()
    l= [None] * (len(arr))
    print(l)
    for i in range(len(arr)):
        word=arr[i]
        num=int(word[-1])-1
        l[num]= arr[i][:-1]
    return ' '.join(l)

print(sort_array("Myself2 Me1 I4 and3"))


