class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        composites = set()
            
        for i in range(3,int(sqrt(right))+1,2):
            prod = i*i
            while prod<=right:
                if prod>=left:
                    composites.add(prod)
                prod+=i*2
        primes = []
        if left<=2 and right>=2:
            primes.append(2)
        for num in range(left,right+1):
            if num not in composites and num%2==1 and num!=1:
                primes.append(num)
        diff=float('inf')
        ans = [-1,-1]
        for i in range(1,len(primes)):
            if primes[i]-primes[i-1] < diff:
                diff = primes[i]-primes[i-1]
                ans = [primes[i-1],primes[i]]
                
        return ans

            
        
        
        
