
# generate the encryption table with the key
def generateKeyTable(key):
    finalResult=""
    d={}
    for i in key:
        d[i] = d.get(i,0) +1
        if d[i] <2: finalResult += i
        
    for i in range(25):
        if chr(i + 97) not in d:
            finalResult += chr(i+97)        
    print("--->",finalResult)
    lst = [i for i in finalResult]    
    matrix =[]
    while lst:
        matrix.append(lst[:5])
        lst = lst[5:]    
    return matrix
    
# print(generateKeyTable("hallo") ) 

# group input string into 2 elements of a string & pad if it is duplicate
def splitAndCleanMessage(text):
    arr=[]
    N = len(text) if len(text)%2 ==0 else len(text)-1
    for i in range(0,N, 2):
        arr.append(text[i:i+2])
    
    for i in range(N//2):
        a,b = arr[i]
        if a==b:
            arr[i]=a+"x"
    if N != len(text):
        arr.append(text[-1] +"x")    
    return arr
# print(splitAndCleanMessage("newteey"))
    
    
    
    
def findIndexOfItem(Matrix, val):
    zx, zy = 0,0
    for i in range(5):
        for j in range(5):
            if(Matrix[i][j] == val):
                return i, j
            if(Matrix[i][j] == 'x'):
                zx, zy = i,j
    return zx, zy
                
    
    
# encrypt values in the same row
def encryptSameRow(Matrix, row, col):
    enc1 = Matrix[row][0] if col ==4 else Matrix[row][col +1]    
    return enc1

# encrypt values in the same col
def encryptSameCol(Matrix, row, col):    
    enc1 = Matrix[0][col] if row ==4 else Matrix[row + 1][col] 
    # print("enc1--", enc1)   
    return enc1
# encrypt on the rectangle rule: takes index & row & return the row & col of encryption
def encryptOnRectangle(Matrix, v1row, v1col, v2row, v2col):
    enc1 = Matrix[v1row][v2col]
    enc2 = Matrix[v2row][v1col]
    return enc1, enc2



def enctypt(key, plainText):
    finalText =""
    plainText = "".join(plainText.split())
    plainText.lower()
    key = "".join(key.split())
    key=key.lower()    
    encryptionTable = generateKeyTable(key)
    print("encTable==>", encryptionTable)
    cleanedMessage = splitAndCleanMessage(plainText)
    print(cleanedMessage)
    for v1, v2 in cleanedMessage:
        enc1 , enc2 = "", ""
        
        i1row, i1col =findIndexOfItem(encryptionTable, v1)
        i2row, i2col =findIndexOfItem(encryptionTable, v2)
        
        if i1row == i2row:
            enc1 = encryptSameRow(encryptionTable, i1row, i1col)
            enc2 = encryptSameRow(encryptionTable, i2row, i2col)
        elif i1col == i2col:
            # print("i1,12-", v1,v2, i1row, i1col)
            enc1 = encryptSameCol(encryptionTable, i1row, i1col)
            enc2 = encryptSameCol(encryptionTable, i2row, i2col)
        else:
            enc1 , enc2 = encryptOnRectangle(encryptionTable, i1row, i1col, i2row, i2col)
        
        finalText += (enc1 +enc2)
    return finalText
        
        
print(enctypt("key","ztoday is good dayz"))