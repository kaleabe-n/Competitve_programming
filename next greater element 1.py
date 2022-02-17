class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in (nums1):
            ind = nums2.index(i)
            j = ind
            while j<len(nums2):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    break
                elif j == len(nums2)-1:
                    ans.append(-1)
                j+=1

        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
