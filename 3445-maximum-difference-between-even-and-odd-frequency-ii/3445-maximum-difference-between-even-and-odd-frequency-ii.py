class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        l = len(s)
        dp = [0] * (l)
        sm = [0] * 5
        for i, j in enumerate(s):
            sm[int(j)] += 1
            dp[i] = sm.copy()
        prev = [[defaultdict(lambda: -math.inf) for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if dp[-1][i] > 0 and dp[-1][j] > 0:
                    need = str(dp[-1][i] % 2) + str(dp[-1][j] % 2)
                    prev[i][j][need] = [(dp[-1][i], dp[-1][j])]

        mx = -math.inf
        r = l - 1
        for i in range(l - k, -1, -1):
            for m in range(5):
                for n in range(5):
                    prev_m = dp[i - 1][m] if i - 1 >= 0 else 0
                    prev_n = dp[i - 1][n] if i - 1 >= 0 else 0
                    a, b = str((prev_m + 1) % 2), str(prev_n % 2)
                    if prev[m][n][a + b] != -math.inf:
                        for values in prev[m][n][a + b]:
                            (rr, q) = values
                            odd, even = rr - prev_m, q - prev_n
                            if odd > 0 and even > 0:
                                sm = odd - even
                                if sm > mx:
                                    mx = sm
            r -= 1
            for m in range(5):
                for n in range(5):
                    if dp[r][m] > 0 and dp[r][n] > 0:
                        need = str(dp[r][m] % 2) + str(dp[r][n] % 2)
                        if prev[m][n][need] == -math.inf:
                            prev[m][n][need] = [(dp[r][m], dp[r][n])]
                        else:
                            mn = math.inf
                            mn_index = None
                            for index, values in enumerate(prev[m][n][need]):
                                (a, b) = values
                                hold = a - b
                                if hold < mn:
                                    mn = hold
                                    mn_index =  index
                            if len(prev[m][n][need]) == 2:
                                oth = 0 if mn_index == 1 else 1
                                if dp[r][m] - dp[r][n] > mn and prev[m][n][need][oth] != (dp[r][m], dp[r][n]):
                                    prev[m][n][need][mn_index] = (dp[r][m], dp[r][n])
                            else:
                                if dp[r][m] - dp[r][n] > mn:
                                    prev[m][n][need].append((dp[r][m], dp[r][n]))
        return mx   