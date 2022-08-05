class Solution(object):
    def hIndex(self, citations):
        left = 0
        right = len(citations)-1
        while right>left:
            
            if citations[(left+right)//2]<len(citations)-(left+right)//2:
                if citations[(left+right)//2+1]>=len(citations)-(left+right)//2-1:
                    return len(citations)-((left+right)//2+1)
                else:
                    left = (left+right)//2+1
            else:
                right = (left+right)//2
        if right == left and citations[left]>=len(citations)-left:
            return len(citations)-left
        return 0
        """
        :type citations: List[int]
        :rtype: int
        """
        
