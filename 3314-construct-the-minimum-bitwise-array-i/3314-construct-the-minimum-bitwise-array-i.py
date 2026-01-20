class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return [n&(n+1)|(~n&(n+1))//2-1 for n in nums]    