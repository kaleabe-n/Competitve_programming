class Solution(object):
    def reverseParentheses(self, s):
        openingIndices=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                openingIndices.append(i)
                i+=1
            elif s[i]==')':
                left=s[:openingIndices[-1]]
                right=s[i+1:]
                centre=s[openingIndices[-1]+1:i]
                centre=centre[::-1]
                s=left+centre+right
                openingIndices.pop()
                i-=1
            else:
                i+=1
        return s
        """
        :type s: str
        :rtype: str
        """
        
