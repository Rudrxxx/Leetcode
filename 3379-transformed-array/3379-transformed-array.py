class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = nums.copy()

        for i in range(n):
            if(nums[i] > 0):
                rightSteps = nums[i]
                newIndex = (i + rightSteps) % n

                result[i] = nums[newIndex]
            elif(nums[i] < 0):
                leftSteps = abs(nums[i])
                newIndex = ((i - leftSteps) % n) + n % n

                result[i] = nums[newIndex]
            else:
                result[i] = nums[i]
        
        return result