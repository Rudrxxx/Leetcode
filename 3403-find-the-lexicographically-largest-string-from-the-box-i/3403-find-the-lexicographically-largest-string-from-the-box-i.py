class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if(numFriends==1): return word
        maxLen = n-numFriends+1
        res = ""
        for i in range(n):
            res = max(res, word[i:i+maxLen])
        return res