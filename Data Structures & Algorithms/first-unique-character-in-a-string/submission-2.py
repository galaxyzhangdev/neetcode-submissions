class Solution:
    def firstUniqChar(self, s: str) -> int:
        # brute force 
        for i in range(len(s)):
            unique = True
            for j in range(len(s)):
                if i == j:
                    continue
                if s[i] == s[j]:
                    unique = False
                    break
            if unique:
                return i
        return -1