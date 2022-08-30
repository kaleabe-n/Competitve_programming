from collections import defaultdict,deque

class Solution(object):
    def removeDuplicateLetters(self, s):
        lastIndex = defaultdict(lambda : None)
        for i in range(len(s)-1,-1,-1):
            if lastIndex[s[i]] is None:
                lastIndex[s[i]] = i
        stack = deque()
        stackSet = set()
        for i in range(len(s)):
            if s[i] not in stackSet:
                while stack and ord(stack[-1])>=ord(s[i]) and i<lastIndex[stack[-1]] and s[i] not in stackSet:
                    stackSet.remove(stack.pop())
                stack.append(s[i])
                stackSet.add(s[i])
        return "".join(stack)
                
            
        """
        :type s: str
        :rtype: str
        """
