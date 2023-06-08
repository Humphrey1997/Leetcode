# 思路：一位一位的来
# python倒是不存在中间结果超整型变量范围的问题

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            s = 1
        elif x<0:
            s = -1
            x = -x
        else:
            return 0
        flag_end = True
        y = 0
        while x>0:
            t = x%10
            if flag_end and t == 0:
                x = x//10
                continue
            elif flag_end:
                flag_end = False
            y = y*10+t
            x = x//10

        res = s*y
        if res >2**31-1 or res <-2**31:
            return 0
        else:
            return res