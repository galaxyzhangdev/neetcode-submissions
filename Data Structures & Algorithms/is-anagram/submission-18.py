class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force, for loop to compare the sorted strings

        if len(s) != len(t):
            return False
    
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False

        return True

        