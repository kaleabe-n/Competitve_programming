class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queenSet = set()
        attackers = []
        #add the queen locations to set for better lookup time
        for y,x in queens:
            queenSet.add((y,x))
            
        #travel in all 8 possible directions up to distance of 8 in the board to find a queen
        for direction1 in range(1,-2,-1):
            for direction2 in range(1,-2,-1):
                for distance in range(1,8):
                    distY = direction1*distance
                    distX = direction2*distance
                    location = (king[0]+distY,king[1]+distX)
                    if location in queenSet:
                        attackers.append(list(location))
                        break
                        
                        
        return attackers
