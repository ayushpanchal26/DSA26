# link - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n  = len(nums)
        count= 0
        for i in range(1,n):
                if nums[i]<nums[i-1]:
                    count +=1
                    
                
        if nums[n-1]> nums[0]:
            count+=1
        
        if count<=1:
            return True
