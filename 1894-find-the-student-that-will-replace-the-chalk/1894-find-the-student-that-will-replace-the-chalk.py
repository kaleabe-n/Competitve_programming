class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ = sum(chalk)
        k = k%summ
        i = 0
        while k>0:
            if k>=chalk[i]:
                k-=chalk[i]
            else:
                return i
            i = (i+1)%len(chalk)
        return i
            