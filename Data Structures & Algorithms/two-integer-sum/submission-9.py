class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n), O(n)
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i