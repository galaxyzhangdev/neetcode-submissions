class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        sorted_count = sorted(count, key=count.get, reverse=True)
        return sorted_count[:k]
