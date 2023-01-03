class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for j in range(len(strs[0])):
            prev = strs[0][j]
            
            for i in range(1,len(strs)):
                if ord(strs[i][j]) < ord(prev):
                    count+=1
                    break
                    
                prev = strs[i][j]
                
        return count