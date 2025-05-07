class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_time = [[float("inf") for _ in range(n)] for _ in range(m)]
        min_time[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            cur_time, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1: return cur_time
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni == m or nj < 0 or nj == n: continue
                new_time = max(cur_time, moveTime[ni][nj]) + 1
                if min_time[ni][nj] > new_time:
                    min_time[ni][nj] = new_time
                    heapq.heappush(pq, (new_time, ni, nj))
        return 0

