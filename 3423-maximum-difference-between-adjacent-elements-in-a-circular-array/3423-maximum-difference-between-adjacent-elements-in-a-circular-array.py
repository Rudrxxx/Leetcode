class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxx = float('-inf')
        for i in range(len(nums)-1):
            maxx = max(maxx, abs(nums[i] - nums[i + 1]))
        maxx = max(maxx, abs(nums[-1] - nums[0]))
        return maxx