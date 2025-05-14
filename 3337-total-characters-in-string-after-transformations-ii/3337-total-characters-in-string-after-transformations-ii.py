mod = 10 ** 9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        #make the transfer matrix
        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T[i][(i + j) % 26] = 1

        #make the original matrix
        orig = [[0] * 26 for _ in range(26)]
        for i in range(26):
            orig[i][i] = s.count(chr(ord("a") + i))

        #exponentiation on calculatin orig * (T ** t)
        while t > 0:
            if t % 2 == 1:
                orig = self.matrix_multiply_mod(orig, T)
            T = self.matrix_multiply_mod(T, T)
            t //= 2

        #fetch result
        ans = 0
        for i in range(26):
            for j in range(26):
                ans += orig[i][j]
                ans %= mod
        return ans

#matrix multiplication helper function
    def matrix_multiply_mod(self, A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])

        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod

        return result
        