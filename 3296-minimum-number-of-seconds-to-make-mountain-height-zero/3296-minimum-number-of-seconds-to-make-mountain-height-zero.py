class Solution:
    def minNumberOfSeconds(self, mH: int, workerTimes: List[int]) -> int:
        cnt   = Counter(workerTimes).most_common()
        lo,hi = 0, cnt[-1][0]*mH*(mH+1)//2 +1
        while  lo < hi:
            t = (lo + hi)//2 *8
            if  sum((floor(sqrt(1+t/w)) -1)//2 *wn for w,wn in cnt) >= mH: hi = t//8
            else:                                                          lo = t//8 +1
        return lo
        