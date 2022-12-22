class Solution:
    def countDigitOne(self, n: int) -> int:
        n = str(n)
        n = [int(x) for x in n]
        if n == 0:
            return 0
        prev = 0
        for i in range(-len(n),0,1):
            if n[i]>1:
                temp = 10 ** (-i-1)
            elif n[i] == 1:
                l = [str(x) for x in n[i+1:]]
                temp = int("".join(l)) if i<-1 else 0
                temp+=1
            else:
                temp = 0
            temp+=(10**(-i-2))*(-i-1)*n[i] if -i >=2 else 0
            prev+=temp
        return prev
            
        