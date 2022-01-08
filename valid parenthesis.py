class Solution(object):
    def isValid(self, s):
        li = []
        openings = ['(', '{', '[']
        closings = [')', '}', ']']
        for i in s:
            if i in openings:
                li.append(i)
            elif i in closings:
                if len(li) == 0:
                    return False
                elif li[-1] == openings[closings.index(i)]:
                    li.pop()
                else:
                    return False
        if len(li) > 0:
            return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        
