class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        c=0
        x=l=r=-1
        for i,num in enumerate(nums):
            if not minK<=num<=maxK:
                x=i
            if num==minK:
                l=i
            if num==maxK:
                r= i
            c+=max(0,min(l,r)-x)
        return c