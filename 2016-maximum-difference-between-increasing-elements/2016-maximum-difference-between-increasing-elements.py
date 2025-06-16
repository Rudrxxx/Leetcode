class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        low = float('inf')
        for i in nums:
            if i < low:
                low = i
            elif low < i:
                val = i - low
                result = val if val > result else result
        return result
