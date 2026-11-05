class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in map:
                map[nums[i]] = i
            else:
                return [map[diff], i]
                    
