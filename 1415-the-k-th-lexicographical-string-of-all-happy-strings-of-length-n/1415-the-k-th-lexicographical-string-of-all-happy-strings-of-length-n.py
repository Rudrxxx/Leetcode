class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        sz = 3 * (1 << (n - 1))
        if k > sz:
            return ""

        base = 1 << (n - 1)
        q = (k - 1) // base
        r = (k - 1) % base

        s = [''] * n
        s[0] = chr(ord('a') + q)

        xx = [
            ['b', 'c'],
            ['a', 'c'],
            ['a', 'b']
        ]

        for i in range(n - 2, -1, -1):
            idx = ord(s[n - 2 - i]) - ord('a')
            bit = (r >> i) & 1
            s[n - 1 - i] = xx[idx][bit]

        return ''.join(s)