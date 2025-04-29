class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m=max(nums)
        c=0
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==m:
                c+=1
            while c>=k:
                ans+=len(nums)-r
                if nums[l]==m:
                    c-=1
                l+=1
        return ans