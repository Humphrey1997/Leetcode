# 思路：滑动窗口，用dict实现，只要新加入的元素有重复，就删除最左边的元素
# 收获：熟悉set数据结构

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s

        left = 0
        right = 1
        maxlen = 1
        d = set()
        d[s[0]] = 0

        while right < len_s:
            while s[right] in d:
                d.remove(s[left])
                left += 1
            nowlen = right - left + 1
            maxlen = max(maxlen,nowlen)
            d.add(s[right])
            right += 1
        return maxlen