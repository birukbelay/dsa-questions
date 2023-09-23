import sys, threading

input = lambda: sys.stdin.readline().strip()

arr =[]
def fun(a,b):
    if a==b:
        arr.append(a)
        return
    if (a*10) +1==b:
        
        
def main():
    # write your code here
    a, b = [int(a) for a in input().split()]
    print(a,b)

if __name__ == '__main__':    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()