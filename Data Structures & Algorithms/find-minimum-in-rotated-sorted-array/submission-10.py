class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                # min in the left
                r = m
            else:
                # min in the right
                l = m + 1
        return nums[l]

        