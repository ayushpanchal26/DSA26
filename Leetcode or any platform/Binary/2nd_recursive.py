#link - https://leetcode.com/problems/binary-search/
def binary_search(self,nums,low,high,target):
        if low>high:
            return -1 
        mid = (low+high)//1
        if target == nums[mid]:
            return mid
        elif target>nums[mid]:
            return self.binary_search(nums,mid+1,high,target)
        return self.binary_search(nums,low,mid-1,target)
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums,0 , len(nums)-1,target)