class Solution(object):
    def minimumRecolors(self, blocks, k):
        prefixBlackCount = []
        prefixCount = 0
        for i in blocks:
            if i == 'W':
                prefixCount+=1
            prefixBlackCount.append(prefixCount)
        prefixBlackCount.append(0)
        minn = float('inf')
        for i in range(k-1,len(blocks)):
            minn = min(minn,prefixBlackCount[i]-prefixBlackCount[i-k])
        return minn
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        