class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        brocken = False
        for i in range(200):
            if i >=len(strs[0]):
                break
            temp = strs[0][i] 
            for word in strs:
                if i>=len(word) or word[i] != temp:
                    brocken = True
                    break
            else:
                ans+=temp
            if brocken:
                break
        return ans
