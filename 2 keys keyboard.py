class Solution:
    def minSteps(self, n: int) -> int:
        primes = []
        for i in range(2,n//2):
            while n%i == 0:
                primes.append(i)
                n//=i
        if n>1:
            primes.append(n)
            
        return sum(primes)
            
            
