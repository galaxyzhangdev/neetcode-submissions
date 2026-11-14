class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                      
        res = []                        

        for i in range(len(nums)):
            # i > 0：i = 0 前面没有元素，不能和 nums[-1] 比，它一定是第一次出现，必须处理
            # nums[i] == nums[i-1]：和前一个相同，说明这个值已经处理过了
            # continue：结束这一轮，后面的 l, r 赋值和 while 都不执行，旧的 l, r 没人用
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            # l < r，不用 !=：偶数长度时指针会交叉而不是相遇，!= 永远不会变 False，会越界
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1               # 和太小：排序后右边的数更大，所以移动左指针
                elif total > 0:
                    r -= 1               # 和太大：左边的数更小，所以移动右指针
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1               
                    # 跳过和刚用过的 nums[l-1] 相同的值，避免同一个 i 输出重复三元组
                    # 用 while 不用 if：重复的值可能连续出现多个
                    # l < r：防止 l 越过 r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
