class Solution:
    def firstUniqChar(self, s: str) -> int:
        # brute force
        for i in range(len(s)):
            flag = True
            for j in range(len(s)):
                if i == j:
                    continue
                if s[i] == s[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1
            