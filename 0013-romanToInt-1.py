# 思路：如果当前字符代表的数值小于下一个字符代表的数值，则将当前字符代表的数值取反，并加上下一个字符代表的数值，然后将索引向后移动两位。例如，"IV" 表示 4，"IX" 表示 9。如果当前字符代表的数值大于或等于下一个字符代表的数值，则将当前字符代表的数值累加，并将索引向后移动一位。

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        num = 0
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
                num += roman_values[s[i+1]] - roman_values[s[i]]
                i += 2
            else:
                num += roman_values[s[i]]
                i += 1
        
        return num
