# 思路：反转一半数字，当原始数字小于或等于反转后的数字时，就意味着已经处理了一半位数的数字

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        #分位数为奇数和偶数两种情况
        return x == revertedNumber or x == revertedNumber // 10
