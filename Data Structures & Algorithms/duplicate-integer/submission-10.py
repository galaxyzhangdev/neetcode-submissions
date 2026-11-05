class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## brute force, for loop to compare i j, O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        ## use sort and compare, O(n log n)
        # nums_sort = sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        ## use set to check if duplicates are exsiting, O(n)
        # return len(nums) != len(set(nums))

        ## better set option, search at the same time
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False