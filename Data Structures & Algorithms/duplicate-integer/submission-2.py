class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = []
        for i in nums:
            if i in l:
                return True
            l.append(i)
        return False