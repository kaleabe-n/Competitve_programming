class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0"*(len(a)-len(b)) + b
        if len(a) < len(b):
            a = "0" * (len(b)-len(a)) + a
        rem = 0
        ans = []
        for i in range(len(a)-1,-1,-1):
            curr = int(a[i]) + int(b[i]) + rem
            rem = curr//2
            ans.append(str(curr % 2))
        if rem:
            ans.append(str(rem))
        ans.reverse()
        return "".join(ans)