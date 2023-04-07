class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 1
        ans = 0
        negCount = 0
        for _ in range(32):
            count = 0
            for num in nums:
                if num<0:
                    num = -num
                    negCount+=1
                if num & mask:
                    count += 1
                
            if count % 3:
                ans+=mask
            mask<<=1
        if negCount%3:
            ans = -ans
        return ans
                
