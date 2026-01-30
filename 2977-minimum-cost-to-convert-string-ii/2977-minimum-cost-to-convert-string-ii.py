class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int]
    ) -> int:
        n = len(source)
        INF = 10**18
        strs = set(original) | set(changed)
        sid = {s: i for i, s in enumerate(strs)}
        m = len(sid)
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            u, v = sid[o], sid[c]
            dist[u][v] = min(dist[u][v], w)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    if dist[k][j] == INF:
                        continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd
        rules = {}
        for o, c in zip(original, changed):
            L = len(o)
            rules.setdefault(L, []).append((sid[o], sid[c]))
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]
            for L, pairs in rules.items():
                j = i - L
                if j < 0:
                    continue
                ssub = source[j:i]
                tsub = target[j:i]
                if ssub in sid and tsub in sid:
                    u, v = sid[ssub], sid[tsub]
                    if dist[u][v] < INF:
                        dp[i] = min(dp[i], dp[j] + dist[u][v])

        return -1 if dp[n] == INF else dp[n]