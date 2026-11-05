class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            prod = 1
            nums_copy = nums.copy()
            nums_copy.remove(num)
            for i in (nums_copy):
                prod = prod * i
            res.append(prod)
        return res