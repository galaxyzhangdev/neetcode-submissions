class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the purpose is if we have seen the number, so we can use complment number and dict, time
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i