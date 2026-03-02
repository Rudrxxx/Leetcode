class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # trailing_zeros[i] = number of trailing zeros in row i
        trailing_zeros = []
        for row in grid:
            tz = 0
            j = n - 1
            while j >= 0 and row[j] == 0:
                tz += 1
                j -= 1
            trailing_zeros.append(tz)

        swaps = 0

        # For each row position i, we need at least (n-1-i) trailing zeros
        for i in range(n):
            need = n - 1 - i

            # Find the first row j >= i that satisfies the requirement
            j = i
            while j < n and trailing_zeros[j] < need:
                j += 1

            if j == n:
                return -1  # impossible

            # Bring row j up to i using adjacent swaps
            swaps += (j - i)

            # Simulate the swaps by moving trailing_zeros[j] to position i
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                j -= 1

        return swaps