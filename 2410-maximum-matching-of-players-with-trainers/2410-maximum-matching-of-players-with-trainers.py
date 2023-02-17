class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matchings = 0
        c = 0
        for player in players:
            while c<len(trainers) and trainers[c] < player:
                c+=1
            if c>=len(trainers):
                break
            if trainers[c] >= player:
                matchings+=1
                c+=1
        return matchings