# link - https://leetcode.com/problems/binary-search/submissions/1403145867/
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                low  = mid+1
            else:
                high = mid-1
        return -1