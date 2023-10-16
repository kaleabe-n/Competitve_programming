class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        count = 0
        prefs = [[0]*(n) for _ in range(n)]
        for i in range(n):
            for j,val in enumerate(preferences[i]):
                prefs[i][val] = j
        pairing = [0]*n
        for l,r in pairs:
            pairing[l] = r
            pairing[r] = l
        for l,r in pairs:
            for item in preferences[l]:
                if item == r:
                    break
                if prefs[item][pairing[item]] > prefs[item][l]:
                    count += 1
                    break
            for item in preferences[r]:
                if item == l:
                    break
                if prefs[item][pairing[item]] > prefs[item][r]:
                    count += 1
                    break
        return count
