from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = ["."]*len(dominoes)
        que = deque()
        count = [0] *len(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                que.append([i,dominoes[i],1])
                count[i] = 1
        while que:
            ind,direction,countCurr = que.popleft()
            if direction == "L":
                if ans[ind] == "L":
                    continue
                elif count[ind] == countCurr and count[ind]!=0 and ans[ind] == "R":
                    ans[ind] = '.'
                    continue
                elif ans[ind] == "R":
                    continue
                elif ans[ind] == '.':
                    ans[ind] = 'L'
                    count[ind] = countCurr
                    if ind>0:
                        que.append([ind-1,"L",countCurr+1])
            if direction == "R":
                if ans[ind] != ".":
                    continue
                else:
                    ans[ind] = "R"
                    if ind<len(dominoes)-1:
                        que.append([ind+1,"R",countCurr+1])
                    count[ind] = countCurr
                
        return "".join(ans)
                
                
        