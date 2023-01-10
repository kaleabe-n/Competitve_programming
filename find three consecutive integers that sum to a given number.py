class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        num2 = num // 3
        if num2 * 3 == num:
            return [num2-1,num2,num2+1]
        return []
