def xor(x1, x2):
    if(x1 and x2) or (not x1 and not x2):
        return False
    return True

print(xor(True, True))
print(xor(False, False))
print(xor(True, False))
print(xor(False, True))


print(xor(5,10))
print(xor(5,0))