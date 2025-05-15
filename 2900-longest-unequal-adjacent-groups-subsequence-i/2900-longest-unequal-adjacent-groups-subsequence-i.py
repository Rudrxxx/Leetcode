class Solution:
    def getLongestSubsequence(self, words, groups):
        def build_sequence(s):
            r=[]
            e=s
            for i in range(len(words)):
                if groups[i]==e:
                    r.append(words[i])
                    e^= 1
            return r
        seq1 = build_sequence(0)
        seq2 = build_sequence(1)
        return seq1 if len(seq1) >= len(seq2) else seq2