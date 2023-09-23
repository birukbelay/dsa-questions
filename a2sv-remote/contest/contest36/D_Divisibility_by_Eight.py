import sys
input = sys.stdin.readline
# from collections import Counter

n= input().strip()

def is_divisible(num_str):
    num = int(num_str)
    return num %8==0


def find_divisible_subset(num_str):
    if is_divisible(num_str):
        return num_str
    n = len(num_str)
    for i in range(n):
        if is_divisible(num_str[i]):
            return num_str[i]
        for j in range(i+1, n):
            if is_divisible(num_str[i] + num_str[j]):
                return num_str[i] + num_str[j]
            for z in range(j+1, n):
                if is_divisible(num_str[i] + num_str[j] + num_str[z]):
                    return num_str[i] + num_str[j] + num_str[z]
    return None

res  = find_divisible_subset(n)
if res =='0' or (res and res[0]!='0'):
    print('YES')
    print(res)
else:
    print('NO')