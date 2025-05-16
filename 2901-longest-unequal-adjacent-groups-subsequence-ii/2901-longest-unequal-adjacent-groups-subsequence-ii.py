from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n            
        parent = [-1] * n       
        def hamming_distance(a: str, b: str) -> int:
            return sum(x != y for x, y in zip(a, b))
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming_distance(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
        max_len = max(dp)
        idx = dp.index(max_len)
        result = []
        while idx != -1:
            result.append(words[idx])
            idx = parent[idx]
        return result[::-1]