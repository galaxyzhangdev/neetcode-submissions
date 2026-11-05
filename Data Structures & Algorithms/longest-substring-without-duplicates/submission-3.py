class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         sub = s[i:j]
        #         # which means no duplicates
        #         if len(sub) == len(set(sub)):
        #             res = max(res, len(sub))
        # return res
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
