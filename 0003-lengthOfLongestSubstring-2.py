# 思路：滑动窗口，用dict实现，与方法1不同的是直接定位重复元素的位置，然后把左边的全删掉。方法1每删掉一个，都要再查询一次，而方法2不用

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s

        left = 0
        right = 1
        maxlen = 1
        d = dict()
        d[s[0]] = 0

        while right < len_s:
            if s[right] in d:
                nowlen = right - left
                for i in range(left,d[s[right]]):
                    del d[s[i]]
                left = d[s[right]] + 1
            else:
                nowlen = right - left + 1
            maxlen = max(maxlen,nowlen)
            d[s[right]] = right
            right += 1
        return maxlen






