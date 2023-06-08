#思路：
# 首先，创建一个字典 phone，将数字与对应的字母映射关系存储起来。
# 然后，创建两个列表，result 用于存储最终的字母组合，current 用于存储当前已生成的组合。
# 接下来，遍历数字字符串 digits 中的每个数字。对于每个数字，从 current 列表中取出当前已生成的组合，然后根据当前数字获取对应的字母列表。
# 对于每个已生成的组合，将其与当前数字对应的每个字母进行拼接，并将拼接结果存入 result 列表中。
# 最后，将 result 赋值给 current，继续下一个数字的处理。重复上述步骤，直到遍历完所有数字

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        if digits[0] in phone:
            result = phone[digits[0]]

        for i in range(1, len(digits)):
            current = result
            result = []
            if digits[i] in phone:
                for combination in current:
                    for letter in phone[digits[i]]:
                        result.append(combination + letter)

        return result