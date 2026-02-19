class Solution(object):
    def countBinarySubstrings(self, s):
        groups = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        groups.append(cnt)
        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])
        return res