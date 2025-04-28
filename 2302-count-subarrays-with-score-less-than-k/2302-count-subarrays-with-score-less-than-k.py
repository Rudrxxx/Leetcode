class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr = left = ans = 0
        n = len(nums)
        for right in range(n):
            curr += nums[right]
            while (right-left+1) * curr >= k:
                curr -= nums[left]
                left += 1
            ans += right-left+1
        return ans