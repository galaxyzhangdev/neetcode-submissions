class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            # 如果找到一个有效组合
            if total == target:
                res.append(cur.copy())
                return
            # 如果超出数组范围或总和超过目标值，结束当前路径
            if i >= len(nums) or total > target:
                return
            
            # 选择当前索引的元素
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()  # 回溯
            
            # 不选择当前索引的元素，递归探索下一个索引
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
