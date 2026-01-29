from typing import List
import heapq

class Solution:
    def minimumCost(self, source: str, target: str,
                    from_: List[str], to: List[str], price: List[int]) -> int:

        graph=[[] for _ in range(26)]
        for f,t,p in zip(from_,to,price):
            graph[ord(f)-97].append((ord(t)-97,p))

        INF=10**18
        dist=[[INF]*26 for _ in range(26)]

        def dijkstra(src):
            pq=[(0,src)]
            dist[src][src]=0
            while pq:
                cost,u=heapq.heappop(pq)
                if cost>dist[src][u]: continue
                for v,w in graph[u]:
                    if cost+w<dist[src][v]:
                        dist[src][v]=cost+w
                        heapq.heappush(pq,(dist[src][v],v))

        for i in range(26):
            dijkstra(i)

        ans=0
        for s,t in zip(source,target):
            if s==t: continue
            c=dist[ord(s)-97][ord(t)-97]
            if c==INF: return -1
            ans+=c
        return ans

