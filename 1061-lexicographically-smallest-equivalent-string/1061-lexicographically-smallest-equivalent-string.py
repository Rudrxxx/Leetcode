class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabet = list(string.ascii_lowercase)
        map = {}
        for a in alphabet:
            map[a] = a

        for i in range(0, len(s1)):
            if (map[s1[i]] < map[s2[i]]):
                val = map[s2[i]]
                for j in range(0, 26):
                    if (map[alphabet[j]] == val):
                        map[alphabet[j]] = map[s1[i]]
            elif (map[s2[i]] < map[s1[i]]):
                val = map[s1[i]]
                for j in range(0, 26):
                    if (map[alphabet[j]] == val):
                        map[alphabet[j]] = map[s2[i]]

        sol = ""
        for i in range(0, len(baseStr)):
            sol += map[baseStr[i]]
        return sol