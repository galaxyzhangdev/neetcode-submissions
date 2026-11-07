class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n k log k
        results = defaultdict(list)
        for s in strs: # n
            s_sorted = ''.join(sorted(s)) # k log k
            results[s_sorted].append(s)
        return list(results.values())