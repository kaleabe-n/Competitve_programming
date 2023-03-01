class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            temp = t.lstrip('-')
            if temp.isdigit():
                digit = True
            else:
                digit = False
            
            if digit:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    stack.append(num1+num2)
                elif t == "-":
                    stack.append(num1-num2)
                elif t=="*":
                    stack.append(num1*num2)
                elif t=="/":
                    res = num1/num2
                    res = int(res)
                    stack.append(int(num1/num2))
        return stack[0]
                    
                
