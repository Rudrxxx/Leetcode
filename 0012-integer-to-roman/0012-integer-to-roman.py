class Solution:
    def intToRoman(self, num: int) -> str:
        R= ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                R+= storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return R