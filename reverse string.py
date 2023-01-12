class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-i-1] = s[-i-1],s[i]
        """
        Do not return anything, modify s in-place instead.
        """
