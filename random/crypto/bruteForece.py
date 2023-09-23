def decrypt(text):
    for i in range(26):
        newText=""
        for v in text:
            newText+= CesarsValue(v, i)
        print(newText)

        
       
       


# find encrypted value of char
def CesarsValue(c, key):    
    # val = chr( (ord(c) +key)%97 )

    val = (ord(c)-97 +key)%26
    return chr(97+val)

print(CesarsValue("a", 0))
# print(ord("a"))
# decrypt("bcde")
print(chr(97+25))