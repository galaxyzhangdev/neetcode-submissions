class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## brute force, for loop to compare i j, O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        ## use sort and compare, O(log n)
        nums_sort = nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

        # ## use set to check if duplicates are exsiting O(n)
        # return not len(nums) == len(set(nums))