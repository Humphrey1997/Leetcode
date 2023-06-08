#思路: 将字符串数组的第一个字符串设为当前的最长公共前缀 prefix。从第二个字符串开始遍历字符串数组，比较当前字符串与 prefix 的每个字符是否相等，如果不相等，则将 prefix 更新为当前相同的前缀部分，直到遍历完所有字符串或者 prefix 变为空字符串。

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix