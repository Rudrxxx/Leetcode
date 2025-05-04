class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        ans = 0
        for i in range(len(dominoes)):
            p = tuple(sorted((dominoes[i][0],dominoes[i][1])))
            ans += freq.get(p, 0)
            freq[p] = 1 + freq.get(p, 0)
        return ans