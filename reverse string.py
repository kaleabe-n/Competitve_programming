class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(s,i):
            if i>=(len(s)//2):
                return 
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
            helper(s,i+1)
        helper(s,0)
        """
        Do not return anything, modify s in-place instead.
        """
        


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         for i in range(len(s)//2):
#             s[i],s[-i-1] = s[-i-1],s[i]
#         """
#         Do not return anything, modify s in-place instead.
#         """
