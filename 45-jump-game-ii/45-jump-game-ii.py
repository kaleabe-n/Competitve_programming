class Solution:
    def jump(self, nums: List[int]) -> int:
        reachables = collections.defaultdict(int)
        currJumps=0
        for i in range(len(nums)):
            if reachables[currJumps] >= i:
                if i == len(nums) - 1:
                    return currJumps
                reachables[currJumps+1] = max(reachables[currJumps+1],nums[i] + i)
            else:
                currJumps += 1
                if i == len(nums) - 1:
                    return currJumps
                reachables[currJumps+1] = max(reachables[currJumps+1],nums[i] + i)
        
                
            