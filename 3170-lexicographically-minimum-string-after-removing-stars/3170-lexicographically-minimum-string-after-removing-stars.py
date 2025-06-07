class Solution:
    def clearStars(self, s: str) -> str:
        heap=[]
        N=len(s)
        removed=[False]*N

        for i in range(N):
            if s[i]=="*":
                v,idx=heappop(heap)
                removed[i],removed[-idx]=True,True
            
            else:
                heappush(heap,(s[i],-i))
        return "".join([s[i] for i in range(N) if not removed[i]])