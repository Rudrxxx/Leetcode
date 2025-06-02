class Solution:
    def candy(self, rating: List[int]) -> int:
        n = len(rating)
        candy = [1] * n
        for i in range(1, n):
            if rating[i] > rating[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if rating[i] > rating[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)