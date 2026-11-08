class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time O(mn), spac O(n or m)
        res = set()
        for n1 in nums1: # n
            for n2 in nums2: # m
                if n1 == n2:
                    res.add(n1)
        return list(res)
        