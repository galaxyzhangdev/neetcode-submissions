class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last = res[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                res.append([start, end])
        return res