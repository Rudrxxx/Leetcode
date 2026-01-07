class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        if n < 4:
            return res
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    total = nums[l]+nums[r]+nums[i]+nums[j]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return res
