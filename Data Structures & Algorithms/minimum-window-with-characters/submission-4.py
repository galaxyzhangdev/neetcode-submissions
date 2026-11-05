class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # helper function to count the char in t
        # def count_t(t):
        #     t_dict = {}
        #     for char in t:
        #         t_dict[char] =  t_dict.get(char,0) + 1
        #     return t_dict
        # # helper function to count char in the sub in t
        # def count_sub(sub, t_dict):
        #     sub_dict = {}
        #     for char in sub:
        #         if char in t_dict:
        #             sub_dict.get(char,0) + 1
        #     for char, count in t_dict.items():
        #         if sub_dict.get(char, 0) < count:
        #             return False
        #     return True

        # t_dict = count_t(t)
        # min_len = 2000
        # res = ""

        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         sub = s[i:j]
        #         if count_sub(sub, t_dict):
        #             if len(sub) < min_len:
        #                 min_len = len(sub)
        #                 res = sub
        # if res:
        #     return res
        # else:
        #     return ""
        def contains_all_chars(substring, t_count):
            sub_count = {}
            # 统计子字符串中的字符频率
            for char in substring:
                if char in t_count:
                    sub_count[char] = sub_count.get(char, 0) + 1
            # 检查子字符串是否满足 t 中所有字符的频率要求
            for char, count in t_count.items():
                if sub_count.get(char, 0) < count:
                    return False
            return True

        # 统计字符串 t 中每个字符的出现频率
        def count_chars(t):
            t_count = {}
            for char in t:
                t_count[char] = t_count.get(char, 0) + 1
            return t_count

        # 主函数逻辑
        t_count = count_chars(t)
        min_len = float('inf')  # 用于记录最小窗口长度
        min_window = ""         # 用于记录最小窗口的子字符串

        # 遍历 s 的所有子字符串
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                # 检查当前子字符串是否包含 t 中的所有字符
                if contains_all_chars(substring, t_count):
                    if len(substring) < min_len:
                        min_len = len(substring)
                        min_window = substring

        return min_window if min_window else ""




        
