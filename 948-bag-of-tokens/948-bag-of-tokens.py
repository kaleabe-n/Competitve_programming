class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        r = len(tokens)-1
        l = 0
        score = 0
        while l<=r and power>=0:
            if power>=tokens[l]:
                power-=tokens[l]
                l+=1
                score+=1
            else:
                if power+tokens[r]>=tokens[l] and l!=r and score>=1:
                    power+=tokens[r]-tokens[l]
                    l+=1
                    r-=1
                else:
                    break
        return score