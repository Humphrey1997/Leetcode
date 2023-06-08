# 思路：用字典保存出现过的数字，对第i个数字查询target-nums[i]是否在字典中
# 收获：熟悉dict这一数据结构

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num],i]
            d[num] = i
        return []