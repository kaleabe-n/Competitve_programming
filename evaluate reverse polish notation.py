import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i.strip("-").isdigit():
                nums.append(int(i))
            else:
                num1 = nums.pop()
                num2 = nums.pop()
                if i == "/":
                    temp = num2/num1
                    if temp > 0:
                        temp = math.floor(temp)
                    else:
                        temp = math.ceil(temp)
                else:
                    temp  = eval(str(num2) + i + str(num1))
                nums.append(temp)
                
        return nums[0]
