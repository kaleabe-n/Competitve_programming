class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = 0
        r = len(piles) - 2
        score = 0
        while l<r:
            score += piles[r]
            l+=1
            r-=2
        return score




# class Solution(object):
#     def maxCoins(self, piles):
#         piles.sort()
#         temp = []
#         new = []
#         while True:
#             temp.append(piles.pop(0))
#             temp.append(piles.pop())
#             temp.insert(1, piles.pop())
#             new.append(temp)
#             temp = []
#             if len(piles) == 0:
#                 break
#         for i in new:
#             piles.append(i[1])
#         s = 0
#         for i in piles:
#             s += i
#         return s
#         """
#         :type piles: List[int]
#         :rtype: int
#         """
        
