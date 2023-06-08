from typing import *
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


        
solu=Solution()

digits = "23"
res = solu.letterCombinations(digits)
print(res)