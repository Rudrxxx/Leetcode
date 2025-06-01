class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def H3(x):
            return 0 if x < 0 else (x + 2) * (x + 1) // 2
        return (H3(n)-3*H3(n-(limit+1))+3*H3(n-2*(limit+1))-H3(n-3*(limit+1)))