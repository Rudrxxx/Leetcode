class Solution:
    def minimumPairRemoval(self, l: List[int]) -> int:
        n = len(l)
        l.append(inf)
        le, ri = list(range(-1, n)), list(range(1, n + 1))
        h = [(a + b, i) for i, (a, b) in enumerate(pairwise(l))]
        heapify(h)

        ans = 0 
        rest = n - sum(1 for a, b in pairwise(l) if a <= b) 

        while rest > 0:
            v, i = heappop(h)
            r = ri[i]
            if le[r] != i or l[i] + l[r] != v:
                continue

            rr = ri[r]
            rest += (l[le[i]] <= l[i]) + (l[i] <= l[r]) + (l[r] <= l[rr])
            le[rr], ri[i] = i, rr
            l[i] = v
            rest -= 1 + (l[le[i]] <= l[i]) + (l[i] <= l[rr])
            if i:
                heappush(h, (l[le[i]] + l[i], le[i]))
            if rr < n:
                heappush(h, (l[i] + l[rr], i))

            ans += 1
        
        return ans