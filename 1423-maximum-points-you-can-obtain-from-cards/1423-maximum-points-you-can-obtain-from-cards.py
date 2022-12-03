class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #this is the length of the array that we will exclude
        lenR = len(cardPoints)-k
        prefixSum = [cardPoints[0]]
        for i in range(1,len(cardPoints)):
            prefixSum.append(prefixSum[-1]+cardPoints[i])
        ans = float('-inf')
        prefixSum.append(0)
        for i in range(k+1):
            ans = max(ans,prefixSum[-2]-(prefixSum[i+lenR-1]-prefixSum[i-1]))
        return ans
        