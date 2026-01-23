class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        idx = {0: [-1, 1]}
        h = [(nums[0] + nums[1], 0)]
        v = [h[0][0]]
        for i in range(1, n - 1):
            idx[i] = [i-1, i+1]
            v.append(nums[i] + nums[i+1])
            h.append((nums[i] + nums[i+1], i))
        idx[n - 1] = [n-2, -1]
        heapify(h)
        ans = 0
        inversions = sum(1 for i in range(n-1) if nums[i] > nums[i+1])
        while inversions > 0:
            while h and (h[0][1] not in idx or h[0][0] != v[h[0][1]]):
                val, i = heappop(h)
                if i in idx and idx[i][1] >= 0:
                    heappush(h, (v[i], i))
            val, i = heappop(h)
            prev, next = idx[i]
            if next >= 0:
                next_next = idx[next][1]
                if nums[i] > nums[next]:
                    inversions -= 1
                idx[i][1] = next_next
                if next_next >= 0:
                    if nums[next] > nums[next_next]:
                        inversions -= 1
                    idx[next_next][0] = i 
                if prev >= 0:
                    if nums[prev] > nums[i]:
                        inversions -= 1
                    idx[prev][1] = i
                idx.pop(next)
                nums[i] = val
                if idx[i][1] >= 0:
                    v[i] = nums[i] + nums[next_next]
                    heappush(h, (v[i], i))
                    if nums[i] > nums[next_next]:
                        inversions += 1
                if prev >= 0:
                    v[prev] = nums[prev] + val
                    if nums[prev] > nums[i]:
                        inversions += 1
                    heappush(h, (v[prev], prev))
                ans += 1
        return ans