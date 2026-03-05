class Solution:
    def help(self, s: str, ch: str) -> int:
        ans = 0
        n = len(s)
        
        for i in range(n):
            if i % 2 == 0 and s[i] != ch:
                ans += 1
            elif i % 2 == 1 and s[i] == ch:
                ans += 1
        
        return ans
    
    def minOperations(self, s: str) -> int:
        opt1 = self.help(s, '0')
        opt2 = self.help(s, '1')
        
        return min(opt1, opt2)