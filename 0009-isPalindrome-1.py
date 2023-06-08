# 思路：直接用python函数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
         # 将整数转换为字符串
        str_x = str(x)
    
        # 比较正序和倒序是否相同
        return str_x == str_x[::-1]