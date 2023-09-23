class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l,r=0,len(tokens)-1
        tokens.sort()
        deque = collections.deque(tokens)
        score=0
        ctr=0
        while l<=r and ctr<len(tokens):
            # print("--",l,r)
            while deque and deque[0]<=power :
                # print("t[l]=", tokens[l], r)
                power-= deque.popleft()
                score+=1
                # l+=1
                # print("sc,",score)
            if score> 0 and l<r:
                # print("-->",score)
                power+=tokens[r]
                score-=1
                r-=1
            ctr+=1
            
        return score
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l,r=0,len(tokens)-1
        tokens.sort()
        deque = collections.deque(tokens)
        score=0
        ctr=0
        while l<=r and ctr<len(tokens):
            # print("--",l,r)
            while  l<=r and tokens[l]<=power :
                # print("t[l]=", tokens[l], r)
                power-=tokens[l]
                score+=1
                l+=1
                # print("sc,",score)
            if score> 0 and l<r:
                # print("-->",score)
                power+=tokens[r]
                score-=1
                r-=1
            ctr+=1
            
        return score