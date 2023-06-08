# 思路：贪心算法,从数组中依次取出数值较大的罗马数字，然后尽可能多地将整数减去该罗马数字，直到整数变为0

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        roman = ''
        i = 0
        
        while num > 0:
            if num >= roman_values[i]:
                roman += roman_symbols[i]
                num -= roman_values[i]
            else:
                i += 1
        
        return roman
