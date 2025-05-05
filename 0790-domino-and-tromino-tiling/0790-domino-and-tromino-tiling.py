class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a0,a1,a2=1,1,2
        ans=0
        for i in range(3,n+1):
            ans=a2*2+a0
            a0=a1
            a1=a2
            a2=ans
        return ans%1000000007