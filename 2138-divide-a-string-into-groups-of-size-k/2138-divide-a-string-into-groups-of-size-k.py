class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i + k] for i in range(0, len(s) - len(s) % k, k)]
        if len(s) % k != 0:
            last = s[len(s) - len(s) % k:]
            last += fill * (k - len(last))
            res.append(last)
        return res