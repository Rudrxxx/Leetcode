class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0

        totalA = 0
        for c in s:
            if c == 'a':
                totalA += 1

        if totalA == 0 or totalA == len(s):
            return 0

        a_right = totalA
        b_left = 0

        ans = min(totalA, len(s) - totalA)

        for c in s:
            if c == 'a':
                a_right -= 1
            else:
                b_left += 1

            ans = min(ans, b_left + a_right)

        return ans