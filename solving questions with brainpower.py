class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]
        for i in range(len(questions)-1,-1,-1):
            points,brainPower = questions[i]
            if brainPower<len(dp)-1:
                curr = dp[-brainPower-1]+points
            else:
                curr = points
            dp.append(max(dp[-1],curr))
        return dp[-1]
            


# class Solution(object):
#     def mostPoints(self, questions):
#         values = [None]*len(questions)
#         for i in range(len(questions)-1,-1,-1):
#             nonSkipped = questions[i][0]+values[i+questions[i][1]+1] if i+questions[i][1]+1 < len(questions) else questions[i][0]
#             skipped = values[i+1] if i<len(questions)-1 else 0 
#             values[i] = max(nonSkipped,skipped)
        
#         return values[0]
#         """
#         :type questions: List[List[int]]
#         :rtype: int
#         """
        
