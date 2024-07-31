class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        orignal = x
        rev = 0
        while x>0:
            last = x%10
            rev = rev*10+last
            x = x//10
            
        return rev

  # https://leetcode.com/problems/reverse-integer/
