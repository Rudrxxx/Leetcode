class Solution:
    MOD = 10**9 + 7

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        # only 0s
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1

        # only 1s
        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1

        for i in range(zero+1):
            for j in range(one+1):
                if i == 0 and j == 0:
                    continue

                if i > 0 and j > 0:
                    ways0 = 0
                    for k in range(1, limit+1):
                        if i-k < 0:
                            break
                        ways0 = (ways0 + dp1[i-k][j]) % self.MOD
                    dp0[i][j] = ways0

                    ways1 = 0
                    for k in range(1, limit+1):
                        if j-k < 0:
                            break
                        ways1 = (ways1 + dp0[i][j-k]) % self.MOD
                    dp1[i][j] = ways1

        return (dp0[zero][one] + dp1[zero][one]) % self.MOD