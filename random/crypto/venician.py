

def keyReverse(key, word):

    ctr=0

    newStr=""

    for i in word:
        

        letter = key[ctr]

        enKey = ord(letter) -97                
        
        val = CesarsValue(i, enKey)        

        newStr+=val
        

        ctr+=1

        if ctr >=len(key): ctr=0
    

    return newStr
        
    

# find encrypted value of char
def CesarsValue(c, key):    

    val = (ord(c)-97 +key)%26    

    # val = chr( (ord(c) +key)%97 )    

    return chr(97+val)


# print(findRev("c", 3))

print(keyReverse("bc", "abcdefg"))