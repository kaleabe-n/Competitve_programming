class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        maxx = 0
        j = 0
        for i in range(len(houses)):
            while j<len(heaters)-1 and houses[i]>=heaters[j+1]:
                j+=1
            if j == len(heaters)-1:
                maxx = max(maxx,abs(heaters[j]-houses[i]))
            else:
                maxx = max(maxx,min(abs(heaters[j]-houses[i]),abs(heaters[j+1]-houses[i])))
        return maxx7
