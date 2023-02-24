class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = collections.defaultdict(int)
        remainders[0]+=1
        prefixSum = 0
        subarrays = 0
        for num in nums:
            prefixSum+=num
            rem = prefixSum%k
            subarrays+=remainders[rem]
            remainders[rem]+=1
        return subarrays
