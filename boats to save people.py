class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount = 0
        i = 0
        j = len(people)-1
        while i<=j:
            if i == j:
                boatCount+=1
                break
            if people[j]+people[i]<=limit:
                boatCount+=1
                j-=1
                i+=1
            else:
                boatCount+=1
                j-=1
        return boatCount
