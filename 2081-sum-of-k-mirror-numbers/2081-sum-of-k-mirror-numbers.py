class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        odd = [i for i in range(k)]
        even = [i*(k + 1) for i in range(k)]

        cnt = k-1

        if n <= cnt:
            return (n *(n+1)) // 2

        sx = (cnt * (cnt + 1)) // 2

        def isPalindrome(x):
            str_x = str(x)
            l = len(str_x)
            for i in range((l + 1) // 2):
                if str_x[i] != str_x[l-1-i]:
                    return False
            return True

        for ev in even:
            if ev != 0 and isPalindrome(ev):
                cnt += 1
                sx += ev
                if cnt == n:
                    return sx

        def generate(arr, cnt, sx, sz):
            new_arr = []
            for i in range(k):
                for num in arr:
                    new_num = num * k + (k**(sz-1) + 1) * i
                    new_arr.append(new_num)
                    if i!=0 and new_num != 0 and isPalindrome(new_num):
                        cnt+=1
                        sx += new_num
                        if cnt == n:
                            return [[], cnt, sx]
            arr.clear()
            return [new_arr, cnt, sx]

             
        for sz in range(3, 31):
            if sz % 2 != 0:
                odd, cnt, sx = generate(odd, cnt, sx, sz)
            else:
                even, cnt, sx = generate(even, cnt, sx, sz)
                
            if n == cnt:
                return sx
        
        return -1
        
        