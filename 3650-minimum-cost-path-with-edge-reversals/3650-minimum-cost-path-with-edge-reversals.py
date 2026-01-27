from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # build graph
        for u, v, w in edges:
            graph[u].append((v, w))   
            graph[v].append((u, 2 * w))
        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)] 

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1