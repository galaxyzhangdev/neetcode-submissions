class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         sub = s[i:j]
        #         freq = {}
        #         for char in sub:
        #             if char in freq:
        #                 freq[char] += 1
        #             else:
        #                 freq[char] = 1
        #         freq_max = max(freq.values())
        #         num_replace = len(sub) - freq_max
        #         if num_replace <= k:
        #             res = max(res, len(sub))
        # return res
        res = 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # get the max freq of each char
            while (r - l + 1) - max(count.values()) > k:
                # remove the left pointer char
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res





        