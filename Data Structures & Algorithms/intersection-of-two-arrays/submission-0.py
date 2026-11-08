class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    res.add(num1)
        return list(res)