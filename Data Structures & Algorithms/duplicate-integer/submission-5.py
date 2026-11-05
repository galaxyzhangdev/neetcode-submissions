class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # if len(set(nums)) == len(nums):
        #     return False
        # return True

        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False

