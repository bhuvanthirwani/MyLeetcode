class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        D={}
        for i in range(len(s)):
            if s[i] in D and D[s[i]] != t[i]:
                return False
            for j in D:
                if D[j] == t[i] and j!=s[i]:
                    return False
            D[s[i]] = t[i]
        return True