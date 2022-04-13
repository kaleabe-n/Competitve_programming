class Solution(object):
    def groupAnagrams(self, strs):
        sW={}
        for i in strs:
            s = str(sorted(i))
            if s in sW:
                sW[s].append(i)
            else:
                sW[s] = [i]
        ans = []
        for i in sW:
            ans.append(sW[i])
        return (ans)
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
