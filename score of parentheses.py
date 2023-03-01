class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for b in s:
            if b == '(':
                stack.append(1)
            elif b == ')':
                curr = stack.pop()
                if curr>1:
                    curr-=1
                if stack:
                    stack[-1]+=2*curr
                else:
                    score+=curr
        return score
