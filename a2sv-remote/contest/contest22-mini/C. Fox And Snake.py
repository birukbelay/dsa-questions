
import sys, threading

input = lambda: sys.stdin.readline().strip()
a, b = [int(a) for a in input().split()]

sw=True
for i in range(a):
    
    if i%2==0:
        print("#"*b)
    else:
        if sw:
            print(  ('.'*(b-1))+'#' )
            sw=False
        else:
            print( '#'+ ('.'*(b-1)) )
            sw=True
            
            