class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        worestIndex = None
        worestGas = None
        currGas = 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if worestIndex == None or currGas <= worestGas:
                worestIndex = i
                worestGas = currGas
        currGas = 0
        for i in range(len(gas)):
            currInd = worestIndex + 1 + i
            currInd = currInd % len(gas)
            currGas += gas[currInd] - cost[currInd]
            if currGas < 0:
                return -1
        return (worestIndex + 1) % len(gas)
