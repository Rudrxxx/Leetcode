class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        mx=d=0
        t=k
        for i in s:
            if i=='S' or i=='W':
                if t>0:
                    d+=1
                    t-=1
                else:
                    d-=1
            else:
                d+=1
            if d>mx:
                mx=d
        t=k
        d=0
        for i in s:
            if i=='S' or i=='E':
                if t>0:
                    d+=1
                    t-=1
                else:
                    d-=1
            else:
                d+=1
            if d>mx:
                mx=d
        t=k
        d=0
        for i in s:
            if i=='N' or i=='E':
                if t>0:
                    d+=1
                    t-=1
                else:
                    d-=1
            else:
                d+=1
            if d>mx:
                mx=d
        t=k
        d=0
        for i in s:
            if i=='N' or i=='W':
                if t>0:
                    d+=1
                    t-=1
                else:
                    d-=1
            else:
                d+=1
            if d>mx:
                mx=d
        return mx