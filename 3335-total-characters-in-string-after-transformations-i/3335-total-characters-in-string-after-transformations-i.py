class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        l=1
        mod=10**9+7
        if  len(set(s))==1:
            l=len(s)
            s=s[0]
        def fn(chrs):
            b = [0]*26
            for i in chrs:
                x = ord(i) - ord('a')
                b[x] += 1
            return b
        def fn3(lst):
            b=[0]*26
            n = len(lst)
            ll=[]
            for i in range(n):
                if lst[i]>0:
                    ll.append((i, lst[i]))
            for p,i in ll:
                if p==25:
                    b[0]+=i%mod
                    b[1]+=i%mod
                else:
                    b[p+1]+=i
                b[p]=0 if b[p]-1<0 else b[p]
            return b
        b=fn(s)

        for i in range(t):
            b=fn3(b)
        
        return (sum(b)*l)%mod