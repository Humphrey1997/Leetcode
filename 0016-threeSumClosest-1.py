#思路：还是用排序+双指针，注意剪枝

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        L = len(nums)

        nums.sort()  # 排序数组
        minval = nums[0]+nums[1]+nums[2]
        if L == 3 or minval>=target:
            return minval

        for i in range(len(nums) - 2):            
            left = i + 1
            right = len(nums) - 1
            
            val = nums[i] + nums[i+1] + nums[i+2]
            if val>target and val-target>abs(minval-target):
                break

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val<target:
                    left += 1
                elif val>target:
                    right -= 1
                else:
                    return target
                if abs(val-target)<abs(minval-target):
                    minval = val
                    
        return minval