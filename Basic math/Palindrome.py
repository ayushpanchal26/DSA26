# https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        num = x
        rev = 0
        while x>0:
            last = x%10
            rev = rev*10+last
            num = num//10
            
        return num == rev
