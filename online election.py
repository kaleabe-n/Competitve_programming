class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        self.leadings = []
        leadVote = float('-inf')
        leadPerson = None
        votes = collections.defaultdict(int)
        for i,n in enumerate(persons):
            votes[n] += 1
            if leadVote<=votes[n]:
                leadVote = votes[n]
                leadPerson = n
            self.leadings.append(leadPerson)
            

    def q(self, t: int) -> int:
        l = 0
        r = len(self.times)-1
        while l<=r:
            mid = (l+r)//2
            if self.times[mid]<=t:
                l = mid + 1
            else:
                r = mid-1
        return self.leadings[r]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)




# from collections import defaultdict

# class TopVotedCandidate(object):

#     def __init__(self, persons, times):
#         self.mostVotedPerson = [None]*len(times)
#         self.times = times
#         count = defaultdict(lambda:0)
#         maxCount = 0
#         person = [persons[0]]
#         for i in range(len(times)):
#             count[persons[i]]+=1
#             if count[persons[i]]>=maxCount:
#                 person = persons[i]
#                 maxCount = count[persons[i]]
#             self.mostVotedPerson[i] = person
#         """
#         :type persons: List[int]
#         :type times: List[int]
#         """
        

#     def q(self, t):
#         left = 0
#         right = len(self.times)-1
#         index = None
#         while left<right:
#             if self.times[(left+right)//2]<t:
#                 if self.times[(left+right)//2+1]>t:
#                     index = (left+right)//2
#                     break
#                 else:
#                     left = (left+right)//2+1
#             else:
#                 right = (left+right)//2
#         index = right if index is None else index
#         return self.mostVotedPerson[index]
        
#         """
#         :type t: int
#         :rtype: int
#         """
        


# # Your TopVotedCandidate object will be instantiated and called as such:
# # obj = TopVotedCandidate(persons, times)
# # param_1 = obj.q(t)
