# link - https://leetcode.com/problems/rotate-array/description/
#  leetcode 189
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        k = k%n
        def reverse(p1,p2):
            while(p1<p2):
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p1+=1
                p2-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        