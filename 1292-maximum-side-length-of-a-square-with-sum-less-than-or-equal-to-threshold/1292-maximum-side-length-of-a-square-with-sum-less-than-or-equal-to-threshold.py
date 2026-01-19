class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = mat[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

        length = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                c = length + 1
                if i >= c and j >= c:
                    current_sum = P[i][j] - P[i-c][j] - P[i][j-c] + P[i-c][j-c]
                    if current_sum <= threshold:
                        length += 1
        
        return length