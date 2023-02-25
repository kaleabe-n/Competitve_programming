class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        time = t
        for i,num in enumerate(tickets):
            if i<k:
                time+=min(num,t)
            elif i>k:
                time+=min(num,t-1)
        return time
