class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## brute force, for loop to compare i j, O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        ## use set to check if duplicates are exsiting
        return not len(nums) == len(set(nums))