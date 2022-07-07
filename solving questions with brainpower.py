class Solution(object):
    def mostPoints(self, questions):
        values = [None]*len(questions)
        for i in range(len(questions)-1,-1,-1):
            nonSkipped = questions[i][0]+values[i+questions[i][1]+1] if i+questions[i][1]+1 < len(questions) else questions[i][0]
            skipped = values[i+1] if i<len(questions)-1 else 0 
            values[i] = max(nonSkipped,skipped)
        
        return values[0]
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
