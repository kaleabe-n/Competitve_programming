class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        l = 0
        for r in range(len(s)):
            if s[r]!=s[l]:
                if r-l+1%k == 0:
                    pass
                else:
                    if stack and stack[-1][1] == s[l]:
                        stack[-1][0]+=r-l
                        stack[-1][0]%=k
                        if stack[-1][0] == 0 or stack[-1] == k:
                            stack.pop()
                    else:
                        if (r-l)%k!=0:
                            stack.append([(r-l)%k,s[l]])
                l = r 
        if stack and stack[-1][1] == s[l]:
            stack[-1][0] += r-l+1
        else:
            stack.append([(r-l+1)%k,s[l]])
        if stack[-1][0]%k == 0:
            stack.pop()
        ans = []
        for num,letter in stack:
            ans.append(letter*num)
        return "".join(ans)
            
