class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        nums = set(nums)
        for num in nums:
            temp = num
            for i in range(2,temp // 2 + 1):
                while num%i == 0:
                    primes.add(i)
                    num //= i
            if num == temp:
                primes.add(temp)
        return len(primes)
