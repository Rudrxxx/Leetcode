class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-2):
            if (nums[i]+nums[i+2])*2==nums[i+1]:
                c+=1
        return c