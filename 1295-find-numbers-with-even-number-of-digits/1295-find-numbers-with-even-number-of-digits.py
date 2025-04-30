class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            d=int(math.log10(i))+1
            if d%2==0:
                c+=1
        return c