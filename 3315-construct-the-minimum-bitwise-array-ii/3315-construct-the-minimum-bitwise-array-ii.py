class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            i = 1
            res = -1
            while x&i:
                res = x-i
                i <<= 1
            ans.append(res)
        return ans