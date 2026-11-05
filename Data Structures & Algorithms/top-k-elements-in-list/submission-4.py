class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
        arr = []
        for n,c in hash_map.items():
            arr.append([c,n])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        
        return res