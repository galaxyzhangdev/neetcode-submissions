class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         sub = s[i:j]
        #         if len(set(sub)) == len(sub):
        #             res = max(res, len(sub))
        # return res
        res = 0
        l = 0
        window_set = set()

        for r in range(len(s)):
            # make sure there are no duplicates, so keep removing
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            res = max(res, len(window_set))
        return res