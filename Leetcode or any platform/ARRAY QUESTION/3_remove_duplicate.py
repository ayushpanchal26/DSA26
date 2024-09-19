# link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1,len(nums)):
            if nums[k] != nums[i]:
                k+=1
                nums[k] = nums[i]
        return k+1