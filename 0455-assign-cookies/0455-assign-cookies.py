class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        l,r=0,0
        while l<n and r<m:
            if g[r]<=s[l]:
                r+=1
            l+=1
        return r
