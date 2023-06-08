# 思路：问题很简单，主要是训练格式转换和处理干扰
# 这里是用chatgpt生成的，函数用的很溜，100分

class Solution:
    def myAtoi(self, s: str) -> int:
        # 移除前导空格
        s = s.strip()

        # 检查正负号
        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # 读取数字字符
        result = 0
        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)

        # 处理符号和范围
        result = sign * result
        result = max(min(result, 2**31 - 1), -2**31)

        return result