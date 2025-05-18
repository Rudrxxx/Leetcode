class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod=10**9+7
        def validcol(st):
            for i in range(1,len(st)):
                if st[i]==st[i-1]:
                    return False
            return True
        colors=[0,1,2]
        validst=[]
        for i in product(colors,repeat=m):
            if validcol(i):
                validst.append(i)
        compatible={}
        for i in validst:
            compatible[i]=[]
            for j in validst:
                if all(a!=b for a,b in zip(i,j)):
                    compatible[i].append(j)
        dp=defaultdict(int)
        for i in validst:
            dp[i]=1
        for i in range(n-1):
            newdp=defaultdict(int)
            for j in dp:
                for k in compatible[j]:
                    newdp[k]=(newdp[k]+dp[j])%mod
            dp=newdp
        return sum(dp.values())%mod