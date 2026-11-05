class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case empty
        if t == '':
            return ''
        
        # two hashmaps to record chars
        countT = {}
        window = {}

        # get t chars
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        
        # slide window
        l = 0

        for r in range(len(s)):
            # meet the length condition of t
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # check inside char
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of window to shrink
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ''


                


