# link - https://leetcode.com/problems/search-insert-position/#:~:text=Search%20Insert%20Position%20%2D%20LeetCode&text=Given%20a%20sorted%20array%20of,(log%20n)%20runtime%20complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        ans = n

        while low<= high:
            mid = (high+low)//2
            if nums[mid]>=target:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans
                
