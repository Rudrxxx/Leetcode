class Solution:
    def maxDifference(self, s: str) -> int:
        letterToCount = collections.Counter(s)

        oddMax = 0
        evenMin = inf
        for count in letterToCount.values():
            if count % 2 == 0:
                # Even
                evenMin = min(evenMin, count)
            else:
                # Odd
                oddMax = max(oddMax, count)
        
        return oddMax - evenMin