class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i,num in enumerate(nums):
            if num == k:
                count += 1
            gcd = num
            for j in range(i+1,len(nums)):
                minn = min(gcd,nums[j])
                maxx = max(gcd,nums[j])
                while minn > 0:
                    temp = maxx
                    maxx = minn
                    minn = temp%minn
                gcd = maxx
                if gcd == k:
                    count += 1

        return count
            
