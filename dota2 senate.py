class Solution(object):
    def predictPartyVictory(self, senate):
        bannedIndices = set()
        i = 0
        while len(bannedIndices) < len(senate):
            if senate[i] == "R" and i not in bannedIndices:
                j = (i+1)%len(senate)
                count = 1
                while count>0:
                    if j == i:
                        return "Radiant"
                    if senate[j] == "R" and j not in bannedIndices:
                        count+=1
                    elif senate[j] == "D" and j not in bannedIndices:
                        count-=1
                        bannedIndices.add(j)
                    j+=1
                    j = j%len(senate)
                i=j
            elif senate[i] == "D" and i not in bannedIndices:
                j = (i+1)%len(senate)
                count = 1
                while count>0:
                    if j == i:
                        return "Dire"
                    if senate[j] == "D" and j not in bannedIndices:
                        count+=1
                    elif senate[j] == "R" and j not in bannedIndices:
                        count-=1
                        bannedIndices.add(j)
                    j+=1
                    j = j%len(senate)
                i = j
            if i in bannedIndices:
                i+=1
                i=i%len(senate)
        """
        :type senate: str
        :rtype: str
        """
        
