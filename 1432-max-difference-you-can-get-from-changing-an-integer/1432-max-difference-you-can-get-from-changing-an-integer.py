class Solution:
    def maxDiff(self, num: int) -> int:
        lst = [i for i in str(num)]
        temp1 = False
        c = True
        for j in range(len(lst)):
            if c:
                if lst[j] == '9':
                    continue
                else:
                    temp1 = lst[j]
                    lst[j] = '9'
                    c = False
                    continue
            if temp1 != False:
                if lst[j] == temp1:
                    lst[j] = '9'
        
        ma = int(''.join(lst))

        mn = str(num)

        for i in range(len(mn)):
            if i==0:
                if mn[i]!='1':
                    mn=mn.replace(mn[i],'1')
                    break
            else:
                if mn[i]!='0' and mn[i]!=mn[0]:
                    mn=mn.replace(mn[i],'0')
                    break

        return ma - int(mn)
        