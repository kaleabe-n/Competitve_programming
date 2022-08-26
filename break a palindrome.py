class Solution(object):
    def breakPalindrome(self, palindrome):
        if len(palindrome) == 1:
            return ""
        index = None
        for i in range(len(palindrome)//2):
            if palindrome[i]!="a":
                index = i
                break
        if index is None:
            palindrome = list(palindrome)
            palindrome[-1] = 'b'
            return "".join(palindrome)
        palindrome = list(palindrome)
        palindrome[index] = 'a'
        return "".join(palindrome)
        
        """
        :type palindrome: str
        :rtype: str
        """
        
