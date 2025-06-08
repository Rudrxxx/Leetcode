class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[]
        x=1
        for i in range(n):
            l.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                if x >= n:
                    x //= 10
                x += 1
                while x % 10 == 0:
                    x //= 10
        return l