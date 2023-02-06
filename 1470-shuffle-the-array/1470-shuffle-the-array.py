class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        right = len(nums) // 2
        ans = []
        for left in range(right):
            ans.append(nums[left])
            ans.append(nums[right+left])
        return ans