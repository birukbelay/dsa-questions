import sys
input = sys.stdin.readline
s = input().strip()

# find good part of the array after that
# 1. change all small letters to capital, 
    # leave the ones at the end,
    #  but we can still convert one capital to small in the end part
# 2. change all capital to small

# CCCssCCCCCCCsCCss -3 change the 3 s
# CCCssCCCCCCCssCss -3 change 2s & 1C