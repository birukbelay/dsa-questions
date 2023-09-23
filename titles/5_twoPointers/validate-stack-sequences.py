# https://leetcode.com/problems/validate-stack-sequences/

from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushedQ = deque()
        poppedQ=deque()
        stack=[]
        for i in pushed:
            pushedQ.append(i)
        for j in popped:
            poppedQ.append(j)
        while pushedQ or stack[-1]==poppedQ[0]:
            # print("stack=", stack,"pushedQ==", pushedQ,"poppedQ==",poppedQ  )
            if stack and stack[-1]==poppedQ[0]:
                # print("-------- Popping")
                stack.pop()
                poppedQ.popleft()
                if not(stack or pushedQ or poppedQ):
                    return True                    
            else:
                stack.append(pushedQ.popleft())
        if len(stack)==0:
            return True
        else:
            return False