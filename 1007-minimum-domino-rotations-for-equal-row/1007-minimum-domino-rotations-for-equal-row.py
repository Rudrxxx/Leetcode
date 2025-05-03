class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        val=set()
        x,y=[0]*7,[0]*7
        val.update((tops[0],bottoms[0]))
        res=float("inf")
        for i in range(len(tops)):
            val &={tops[i],bottoms[i]}
            if tops[i] in val and tops[i]!=bottoms[i]:
                y[tops[i]]+=1
            if bottoms[i] in val and tops[i] != bottoms[i]:
                x[bottoms[i]]+=1
        for i in val:
            ans = min(x[i],y[i])
        return ans if val else -1
