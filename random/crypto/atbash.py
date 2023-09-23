
def atbash(str):
    # str.lower()
    d={}
    key=25    
    for i in range(25):              
        d[chr(i+(ord('a')))]=chr(key+65)
        key-=1    
    print(d)
    newStr=''    
    for i in str:
        newStr+=d[i]        
    return newStr

print(atbash("ABC"))
        