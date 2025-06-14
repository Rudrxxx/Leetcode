class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        n = len(s)
        i = 0
        while i < n and s[i] == '9':
            i += 1
        if i < n:
            s = s.replace(s[i], '9')
        t = str(num)
        t = t.replace(t[0], '0')
        return int(s) - int(t)